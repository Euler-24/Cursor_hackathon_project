import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .knowledge import (
    MALADIES_TOMATE,
    diagnostiquer_par_nom_fichier,
    diagnostiquer_par_symptomes,
    galerie,
)
from .models import (
    Culture,
    Diagnostic,
    Maladie,
    Marche,
    Parcelle,
    PrevisionMeteo,
    Prix,
    Recommandation,
    ResultatDiagnostic,
    Utilisateur,
    ZoneMeteo,
)
from .serializers import (
    AnalyseDiagnosticSerializer,
    ConnexionSerializer,
    DiagnosticSerializer,
    MarcheSerializer,
    PrevisionMeteoSerializer,
    PrixSerializer,
    RecommandationSerializer,
    UtilisateurSerializer,
    ZoneMeteoSerializer,
)


def _list_create(request, queryset, serializer_class):
    if request.method == "GET":
        return Response(serializer_class(queryset, many=True).data)

    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def _detail(request, instance, serializer_class, not_found):
    if instance is None:
        return Response({"detail": not_found}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(serializer_class(instance).data)

    if request.method == "DELETE":
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    partial = request.method == "PATCH"
    serializer = serializer_class(
        instance, data=request.data, partial=partial
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def _get_or_none(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        return None


def _assurer_maladie(nom, infos):
    maladie, _created = Maladie.objects.get_or_create(
        nom=nom,
        defaults={
            "description_maladie": infos["cause"],
            "symptomes": ", ".join(infos["symptomes"]),
            "gravite": infos["gravite"],
        },
    )
    Recommandation.objects.get_or_create(
        id_maladie=maladie,
        titre=f"Que faire : {nom}",
        defaults={
            "contenu": infos["conseil"],
            "niveau_urgence": infos["gravite"],
        },
    )
    return maladie


class ConnexionAPIView(APIView):
    def post(self, request):
        serializer = ConnexionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        utilisateur = serializer.validated_data["utilisateur"]
        data = UtilisateurSerializer(utilisateur).data
        data["message"] = "Connexion réussie."
        return Response(data)


class GalerieMaladiesAPIView(APIView):
    def get(self, request):
        return Response({
            "culture": "Tomate",
            "message": (
                "Choisissez la photo qui ressemble à votre plant, "
                "ou décrivez les symptômes."
            ),
            "maladies": galerie(),
        })


class AnalyseDiagnosticAPIView(APIView):
    def post(self, request):
        serializer = AnalyseDiagnosticSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = serializer.validated_data
        id_parcelle = data.get("id_parcelle")
        parcelle = None
        if id_parcelle:
            parcelle = _get_or_none(Parcelle, id_parcelle)
            if parcelle is None:
                return Response(
                    {"detail": "Parcelle introuvable."},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            parcelle = Parcelle.objects.order_by("id_parcelle").first()
            if parcelle is None:
                return Response(
                    {
                        "detail": (
                            "Aucune parcelle n'est enregistrée. "
                            "Créez une exploitation et une parcelle tomate "
                            "avant de lancer un diagnostic."
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        url_image = None
        nom_fichier = ""
        image = data.get("image")
        if image:
            media_dir = os.path.join(settings.MEDIA_ROOT, "diagnostics")
            os.makedirs(media_dir, exist_ok=True)
            storage = FileSystemStorage(location=media_dir)
            nom_fichier = storage.save(image.name, image)
            url_image = request.build_absolute_uri(
                settings.MEDIA_URL + "diagnostics/" + nom_fichier
            )

        symptomes_texte = data.get("symptomes") or ""
        symptomes = [
            s.strip() for s in symptomes_texte.replace(";", ",").split(",")
            if s.strip()
        ]

        matches = []
        methode = "symptomes"
        maladie_directe = None

        if data.get("id_maladie"):
            maladie_directe = _get_or_none(Maladie, data["id_maladie"])
            if maladie_directe is None:
                return Response(
                    {"detail": "Maladie introuvable."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            methode = "galerie"
        elif data.get("numero_galerie"):
            items = galerie()
            numero = data["numero_galerie"]
            choisi = next(
                (item for item in items if item["numero"] == numero),
                None,
            )
            if not choisi:
                return Response(
                    {"detail": "Numéro de galerie invalide."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            infos = MALADIES_TOMATE[choisi["nom"]]
            maladie_directe = _assurer_maladie(choisi["nom"], infos)
            methode = "galerie"
        elif symptomes:
            matches = diagnostiquer_par_symptomes(symptomes)
            methode = "symptomes"
        elif nom_fichier:
            nom, infos = diagnostiquer_par_nom_fichier(nom_fichier)
            if nom:
                maladie_directe = _assurer_maladie(nom, infos)
                methode = "photo"
            else:
                methode = "photo_en_attente"

        diagnostic = Diagnostic.objects.create(
            date_diagnostic=timezone.now(),
            url_image=url_image,
            description_symptomes=symptomes_texte or None,
            statut="termine" if (matches or maladie_directe) else "en_attente",
            id_parcelle=parcelle,
        )

        resultats = []
        if maladie_directe:
            infos = MALADIES_TOMATE.get(maladie_directe.nom, {})
            score = 87 if methode == "photo" else 100
            resultat = ResultatDiagnostic.objects.create(
                id_diagnostic=diagnostic,
                id_maladie=maladie_directe,
                score_confiance=score,
                rang=1,
                est_retenu=True,
            )
            recos = Recommandation.objects.filter(id_maladie=maladie_directe)
            resultats.append({
                "maladie": maladie_directe.nom,
                "score_confiance": float(resultat.score_confiance),
                "rang": 1,
                "cause": infos.get("cause") or maladie_directe.description_maladie,
                "conseils": [r.contenu for r in recos] or [infos.get("conseil")],
                "gravite": maladie_directe.gravite,
            })
        else:
            for rang, (nom, taux, infos) in enumerate(matches, start=1):
                maladie = _assurer_maladie(nom, infos)
                resultat = ResultatDiagnostic.objects.create(
                    id_diagnostic=diagnostic,
                    id_maladie=maladie,
                    score_confiance=round(taux * 100, 2),
                    rang=rang,
                    est_retenu=(rang == 1),
                )
                recos = Recommandation.objects.filter(id_maladie=maladie)
                resultats.append({
                    "maladie": nom,
                    "score_confiance": float(resultat.score_confiance),
                    "rang": rang,
                    "cause": infos["cause"],
                    "conseils": [r.contenu for r in recos] or [infos["conseil"]],
                    "gravite": infos["gravite"],
                })

        avertissement = (
            "Aide à la décision, pas un diagnostic scientifique absolu. "
            "Contactez un agent agricole pour confirmation."
        )
        if methode == "photo_en_attente":
            avertissement = (
                "La reconnaissance automatique par IA n'est pas encore "
                "activée. Utilisez la galerie ou décrivez les symptômes."
            )

        return Response(
            {
                "diagnostic": DiagnosticSerializer(diagnostic).data,
                "methode": methode,
                "resultats": resultats,
                "avertissement": avertissement,
                "galerie": galerie() if not resultats else [],
            },
            status=status.HTTP_201_CREATED,
        )


class ConseilsAPIView(APIView):
    def get(self, request):
        recommandations = Recommandation.objects.select_related(
            "id_maladie"
        ).all()
        data = []
        for reco in recommandations:
            item = RecommandationSerializer(reco).data
            item["maladie"] = reco.id_maladie.nom
            data.append(item)
        return Response(data)


class MarcheListAPIView(APIView):
    def get(self, request):
        return _list_create(request, Marche.objects.all(), MarcheSerializer)

    def post(self, request):
        return _list_create(request, Marche.objects.all(), MarcheSerializer)


class MarcheDetailAPIView(APIView):
    def get(self, request, pk):
        return _detail(
            request, _get_or_none(Marche, pk), MarcheSerializer,
            "Marché introuvable."
        )

    def put(self, request, pk):
        return _detail(
            request, _get_or_none(Marche, pk), MarcheSerializer,
            "Marché introuvable."
        )

    def patch(self, request, pk):
        return _detail(
            request, _get_or_none(Marche, pk), MarcheSerializer,
            "Marché introuvable."
        )

    def delete(self, request, pk):
        return _detail(
            request, _get_or_none(Marche, pk), MarcheSerializer,
            "Marché introuvable."
        )


class PrixListAPIView(APIView):
    def get(self, request):
        queryset = Prix.objects.select_related("id_marche", "id_culture").all()
        id_marche = request.query_params.get("id_marche")
        if id_marche:
            queryset = queryset.filter(id_marche_id=id_marche)
        return Response(PrixSerializer(queryset, many=True).data)

    def post(self, request):
        serializer = PrixSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrixDetailAPIView(APIView):
    def get(self, request, pk):
        return _detail(
            request, _get_or_none(Prix, pk), PrixSerializer, "Prix introuvable."
        )

    def put(self, request, pk):
        return _detail(
            request, _get_or_none(Prix, pk), PrixSerializer, "Prix introuvable."
        )

    def patch(self, request, pk):
        return _detail(
            request, _get_or_none(Prix, pk), PrixSerializer, "Prix introuvable."
        )

    def delete(self, request, pk):
        return _detail(
            request, _get_or_none(Prix, pk), PrixSerializer, "Prix introuvable."
        )


class ZoneMeteoListAPIView(APIView):
    def get(self, request):
        return _list_create(
            request, ZoneMeteo.objects.all(), ZoneMeteoSerializer
        )

    def post(self, request):
        return _list_create(
            request, ZoneMeteo.objects.all(), ZoneMeteoSerializer
        )


class ZoneMeteoDetailAPIView(APIView):
    def get(self, request, pk):
        return _detail(
            request, _get_or_none(ZoneMeteo, pk), ZoneMeteoSerializer,
            "Zone météo introuvable."
        )

    def put(self, request, pk):
        return _detail(
            request, _get_or_none(ZoneMeteo, pk), ZoneMeteoSerializer,
            "Zone météo introuvable."
        )

    def patch(self, request, pk):
        return _detail(
            request, _get_or_none(ZoneMeteo, pk), ZoneMeteoSerializer,
            "Zone météo introuvable."
        )

    def delete(self, request, pk):
        return _detail(
            request, _get_or_none(ZoneMeteo, pk), ZoneMeteoSerializer,
            "Zone météo introuvable."
        )


class PrevisionMeteoListAPIView(APIView):
    def get(self, request):
        queryset = PrevisionMeteo.objects.select_related("id_zone").all()
        id_zone = request.query_params.get("id_zone")
        if id_zone:
            queryset = queryset.filter(id_zone_id=id_zone)
        data = PrevisionMeteoSerializer(queryset, many=True).data
        for item in data:
            humidite = item.get("humidite")
            pluie = item.get("probabilite_pluie")
            risque = "faible"
            if humidite is not None and pluie is not None:
                if float(humidite) >= 80 and float(pluie) >= 50:
                    risque = "eleve"
                elif float(humidite) >= 65 or float(pluie) >= 40:
                    risque = "moyen"
            item["risque_maladie_fongique"] = risque
        return Response(data)

    def post(self, request):
        serializer = PrevisionMeteoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrevisionMeteoDetailAPIView(APIView):
    def get(self, request, pk):
        return _detail(
            request, _get_or_none(PrevisionMeteo, pk),
            PrevisionMeteoSerializer, "Prévision introuvable."
        )

    def put(self, request, pk):
        return _detail(
            request, _get_or_none(PrevisionMeteo, pk),
            PrevisionMeteoSerializer, "Prévision introuvable."
        )

    def patch(self, request, pk):
        return _detail(
            request, _get_or_none(PrevisionMeteo, pk),
            PrevisionMeteoSerializer, "Prévision introuvable."
        )

    def delete(self, request, pk):
        return _detail(
            request, _get_or_none(PrevisionMeteo, pk),
            PrevisionMeteoSerializer, "Prévision introuvable."
        )


class AgentCasAPIView(APIView):
    def get(self, request):
        diagnostics = Diagnostic.objects.select_related(
            "id_parcelle",
            "id_parcelle__id_exploitation",
            "id_parcelle__id_exploitation__id_utilisateur",
        ).order_by("-date_diagnostic")

        cas = []
        for diagnostic in diagnostics:
            exploitation = diagnostic.id_parcelle.id_exploitation
            producteur = exploitation.id_utilisateur
            retenus = list(
                ResultatDiagnostic.objects.select_related("id_maladie").filter(
                    id_diagnostic=diagnostic,
                    est_retenu=True,
                )
            )
            maladie = retenus[0].id_maladie.nom if retenus else None
            score = float(retenus[0].score_confiance) if retenus else None
            cas.append({
                "id_diagnostic": diagnostic.id_diagnostic,
                "date_diagnostic": diagnostic.date_diagnostic,
                "statut": diagnostic.statut,
                "producteur": f"{producteur.prenom} {producteur.nom}",
                "telephone": producteur.telephone,
                "exploitation": exploitation.nom,
                "localisation": exploitation.localisation,
                "parcelle": diagnostic.id_parcelle.nom,
                "maladie": maladie,
                "score_confiance": score,
                "description_symptomes": diagnostic.description_symptomes,
            })
        return Response(cas)


class SanteAPIView(APIView):
    def get(self, request):
        return Response({
            "service": "AgriSence Tomato API",
            "ok": True,
            "cultures": Culture.objects.count(),
            "utilisateurs": Utilisateur.objects.count(),
        })
