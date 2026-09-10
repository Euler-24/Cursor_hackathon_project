from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    Utilisateur,
    Culture,
    Exploitation,
    Parcelle,
    Diagnostic,
    ResultatDiagnostic,
    Recommandation,
    Maladie,
)
from .serializers import (
    UtilisateurSerializer,
    CultureSerializer,
    ExploitationSerializer,
    ParcelleSerializer,
    DiagnosticSerializer,
    ResultatDiagnosticSerializer,
    RecommandationSerializer,
    MaladieSerializer,
)


class CultureListAPIView(APIView):
    def get(self, request):
        cultures = Culture.objects.all()
        serializer = CultureSerializer(cultures, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CultureSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CultureDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            culture = Culture.objects.get(pk=pk)
        except Culture.DoesNotExist:
            return Response(
                {"detail": "Culture introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CultureSerializer(culture)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            culture = Culture.objects.get(pk=pk)
        except Culture.DoesNotExist:
            return Response(
                {"detail": "Culture introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CultureSerializer(culture, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        try:
            culture = Culture.objects.get(pk=pk)
        except Culture.DoesNotExist:
            return Response(
                {"detail": "Culture introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CultureSerializer(
            culture,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            culture = Culture.objects.get(pk=pk)
        except Culture.DoesNotExist:
            return Response(
                {"detail": "Culture introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        culture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExploitationListAPIView(APIView):
    def get(self, request):
        exploitations = Exploitation.objects.all()
        serializer = ExploitationSerializer(exploitations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExploitationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ExploitationDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            exploitation = Exploitation.objects.get(pk=pk)
        except Exploitation.DoesNotExist:
            return Response(
                {"detail": "Exploitation introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ExploitationSerializer(exploitation)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            exploitation = Exploitation.objects.get(pk=pk)
        except Exploitation.DoesNotExist:
            return Response(
                {"detail": "Exploitation introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ExploitationSerializer(
            exploitation,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        try:
            exploitation = Exploitation.objects.get(pk=pk)
        except Exploitation.DoesNotExist:
            return Response(
                {"detail": "Exploitation introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ExploitationSerializer(
            exploitation,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            exploitation = Exploitation.objects.get(pk=pk)
        except Exploitation.DoesNotExist:
            return Response(
                {"detail": "Exploitation introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        exploitation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ParcelleListAPIView(APIView):
    def get(self, request):
        parcelles = Parcelle.objects.all()
        serializer = ParcelleSerializer(parcelles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ParcelleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ParcelleDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            parcelle = Parcelle.objects.get(pk=pk)
        except Parcelle.DoesNotExist:
            return Response(
                {"detail": "Parcelle introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ParcelleSerializer(parcelle)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            parcelle = Parcelle.objects.get(pk=pk)
        except Parcelle.DoesNotExist:
            return Response(
                {"detail": "Parcelle introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ParcelleSerializer(
            parcelle,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        try:
            parcelle = Parcelle.objects.get(pk=pk)
        except Parcelle.DoesNotExist:
            return Response(
                {"detail": "Parcelle introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ParcelleSerializer(
            parcelle,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            parcelle = Parcelle.objects.get(pk=pk)
        except Parcelle.DoesNotExist:
            return Response(
                {"detail": "Parcelle introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        parcelle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DiagnosticListAPIView(APIView):
    def get(self, request):
        diagnostics = Diagnostic.objects.all()
        serializer = DiagnosticSerializer(diagnostics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiagnosticSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class DiagnosticDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            diagnostic = Diagnostic.objects.get(pk=pk)
        except Diagnostic.DoesNotExist:
            return Response(
                {"detail": "Diagnostic introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DiagnosticSerializer(diagnostic)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            diagnostic = Diagnostic.objects.get(pk=pk)
        except Diagnostic.DoesNotExist:
            return Response(
                {"detail": "Diagnostic introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DiagnosticSerializer(
            diagnostic,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        try:
            diagnostic = Diagnostic.objects.get(pk=pk)
        except Diagnostic.DoesNotExist:
            return Response(
                {"detail": "Diagnostic introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DiagnosticSerializer(
            diagnostic,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            diagnostic = Diagnostic.objects.get(pk=pk)
        except Diagnostic.DoesNotExist:
            return Response(
                {"detail": "Diagnostic introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        diagnostic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MaladieListAPIView(APIView):
    def get(self, request):
        maladies = Maladie.objects.all()
        serializer = MaladieSerializer(maladies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MaladieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class MaladieDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            maladie = Maladie.objects.get(pk=pk)
        except Maladie.DoesNotExist:
            return Response(
                {"detail": "Maladie introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MaladieSerializer(maladie)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            maladie = Maladie.objects.get(pk=pk)
        except Maladie.DoesNotExist:
            return Response(
                {"detail": "Maladie introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MaladieSerializer(
            maladie,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        try:
            maladie = Maladie.objects.get(pk=pk)
        except Maladie.DoesNotExist:
            return Response(
                {"detail": "Maladie introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MaladieSerializer(
            maladie,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            maladie = Maladie.objects.get(pk=pk)
        except Maladie.DoesNotExist:
            return Response(
                {"detail": "Maladie introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        maladie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResultatDiagnosticListAPIView(APIView):
    def get(self, request):
        resultatdiagnostics = ResultatDiagnostic.objects.all()
        serializer = ResultatDiagnosticSerializer(
            resultatdiagnostics,
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ResultatDiagnosticSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ResultatDiagnosticDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            resultatdiagnostic = ResultatDiagnostic.objects.get(pk=pk)
        except ResultatDiagnostic.DoesNotExist:
            return Response(
                {"detail": "Resultat diagnostic introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ResultatDiagnosticSerializer(resultatdiagnostic)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            resultatdiagnostic = ResultatDiagnostic.objects.get(pk=pk)
        except ResultatDiagnostic.DoesNotExist:
            return Response(
                {"detail": "Resultat diagnostic introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ResultatDiagnosticSerializer(
            resultatdiagnostic,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        try:
            resultatdiagnostic = ResultatDiagnostic.objects.get(pk=pk)
        except ResultatDiagnostic.DoesNotExist:
            return Response(
                {"detail": "Resultat diagnostic introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ResultatDiagnosticSerializer(
            resultatdiagnostic,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            resultatdiagnostic = ResultatDiagnostic.objects.get(pk=pk)
        except ResultatDiagnostic.DoesNotExist:
            return Response(
                {"detail": "Resultat diagnostic introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        resultatdiagnostic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecommandationListAPIView(APIView):
    def get(self, request):
        recommandations = Recommandation.objects.all()
        serializer = RecommandationSerializer(recommandations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecommandationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class RecommandationDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            recommandation = Recommandation.objects.get(pk=pk)
        except Recommandation.DoesNotExist:
            return Response(
                {"detail": "Recommandation introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = RecommandationSerializer(recommandation)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            recommandation = Recommandation.objects.get(pk=pk)
        except Recommandation.DoesNotExist:
            return Response(
                {"detail": "Recommandation introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = RecommandationSerializer(
            recommandation,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        try:
            recommandation = Recommandation.objects.get(pk=pk)
        except Recommandation.DoesNotExist:
            return Response(
                {"detail": "Recommandation introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = RecommandationSerializer(
            recommandation,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            recommandation = Recommandation.objects.get(pk=pk)
        except Recommandation.DoesNotExist:
            return Response(
                {"detail": "Recommandation introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        recommandation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UtilisateurListAPI(APIView):
    def get(self, request):
        utilisateurs = Utilisateur.objects.all()
        serializer = UtilisateurSerializer(utilisateurs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UtilisateurSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UtilisateurDetailAPI(APIView):
    def get(self, request, pk):
        try:
            utilisateur = Utilisateur.objects.get(pk=pk)
        except Utilisateur.DoesNotExist:
            return Response(
                {"detail": "Utilisateur introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UtilisateurSerializer(utilisateur)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            utilisateur = Utilisateur.objects.get(pk=pk)
        except Utilisateur.DoesNotExist:
            return Response(
                {"detail": "Utilisateur introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UtilisateurSerializer(
            utilisateur,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        try:
            utilisateur = Utilisateur.objects.get(pk=pk)
        except Utilisateur.DoesNotExist:
            return Response(
                {"detail": "Utilisateur introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UtilisateurSerializer(
            utilisateur,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            utilisateur = Utilisateur.objects.get(pk=pk)
        except Utilisateur.DoesNotExist:
            return Response(
                {"detail": "Utilisateur introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        utilisateur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
