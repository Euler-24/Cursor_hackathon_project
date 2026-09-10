from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from .models import (
    Utilisateur,
    Exploitation,
    Parcelle,
    Culture,
    Diagnostic,
    Maladie,
    ResultatDiagnostic,
    Recommandation,
    Marche,
    Prix,
    ZoneMeteo,
    PrevisionMeteo,
)


class CultureSerializer(serializers.ModelSerializer):
    nom = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Culture.objects.all(),
                message="Une culture avec ce nom existe déjà."
            )
        ]
    )

    class Meta:
        model = Culture
        fields = '__all__'

    def validate_nom(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Le nom de la culture ne peut pas être vide"
            )

        if len(value) < 2:
            raise serializers.ValidationError(
                "Le nom de la culture doit contenir au moins 2 caractères"
            )

        return value

    def validate(self, data):
        nom = data.get("nom")
        if nom is None:
            return data

        if str(nom).isdigit():
            raise serializers.ValidationError({
                "nom": (
                    "Le nom d'une culture ne peut pas être composé "
                    "uniquement de chiffres."
                )
            })

        return data


class UtilisateurSerializer(serializers.ModelSerializer):
    mot_de_passe = serializers.CharField(
        write_only=True,
        required=False,
        min_length=6,
        error_messages={
            "min_length": "Le mot de passe doit contenir au moins 6 caractères."
        },
    )
    email = serializers.EmailField(
        required=False,
        allow_null=True,
        allow_blank=False
    )

    role = serializers.ChoiceField(
        choices=[
            ("agriculteur", "Agriculteur"),
            ("agent agricole", "Agent agricole"),
        ]
    )

    telephone = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+?[0-9 ]{8,20}$',
                message="Le numéro de téléphone est invalide."
            )
        ]
    )

    class Meta:
        model = Utilisateur
        exclude = ['mot_de_passe_hash']
        extra_kwargs = {
            'date_inscription': {'read_only': True},
        }

    def validate_nom(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError("Le nom ne peut pas être vide")

        if len(value) < 2:
            raise serializers.ValidationError(
                "Le nom doit contenir au moins 2 caractères"
            )

        return value

    def validate_prenom(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Le prénom ne peut pas être vide"
            )

        if len(value) < 2:
            raise serializers.ValidationError(
                "Le prénom doit contenir au moins 2 caractères"
            )

        return value

    def validate_role(self, value):
        value = value.strip().lower()
        if not value:
            raise serializers.ValidationError(
                "Le rôle ne peut pas être vide."
            )
        return value

    def validate(self, data):
        if self.instance is None and not data.get("mot_de_passe"):
            raise serializers.ValidationError({
                "mot_de_passe": "Le mot de passe est obligatoire."
            })
        return data

    def create(self, validated_data):
        mot_de_passe = validated_data.pop("mot_de_passe")
        validated_data["mot_de_passe_hash"] = make_password(mot_de_passe)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        mot_de_passe = validated_data.pop("mot_de_passe", None)
        if mot_de_passe:
            instance.mot_de_passe_hash = make_password(mot_de_passe)
        return super().update(instance, validated_data)


class ConnexionSerializer(serializers.Serializer):
    telephone = serializers.CharField()
    mot_de_passe = serializers.CharField(write_only=True)

    def validate(self, data):
        telephone = data.get("telephone", "").strip()
        mot_de_passe = data.get("mot_de_passe", "")
        try:
            utilisateur = Utilisateur.objects.get(telephone=telephone)
        except Utilisateur.DoesNotExist:
            raise serializers.ValidationError(
                "Téléphone ou mot de passe incorrect."
            )

        if not check_password(mot_de_passe, utilisateur.mot_de_passe_hash):
            if utilisateur.mot_de_passe_hash != mot_de_passe:
                raise serializers.ValidationError(
                    "Téléphone ou mot de passe incorrect."
                )

        data["utilisateur"] = utilisateur
        return data


class ExploitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exploitation
        fields = '__all__'

    def validate_nom(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Le nom de l'exploitation ne peut pas être vide."
            )
        return value

    def validate_superficie(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError(
                "La superficie ne peut pas être négative."
            )
        return value


class ParcelleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcelle
        fields = '__all__'

    def validate_nom(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Le nom de la parcelle ne peut pas être vide."
            )
        return value

    def validate_superficie(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "La superficie ne peut pas être négative."
            )
        return value


# Alias conservé pour views.py (ancien nom avec typo)
ParcelleSerislizer = ParcelleSerializer


class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostic
        fields = '__all__'
        extra_kwargs = {
            'date_diagnostic': {'required': False},
            'statut': {'required': False},
        }

    def validate_statut(self, value):
        value = value.strip().lower()
        statuts = ["en_attente", "en_cours", "termine", "echec"]
        if value not in statuts:
            raise serializers.ValidationError("Statut invalide.")
        return value

    def create(self, validated_data):
        validated_data.setdefault("date_diagnostic", timezone.now())
        validated_data.setdefault("statut", "en_attente")
        return super().create(validated_data)


class MaladieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maladie
        fields = '__all__'

    def validate_nom(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Le nom de la maladie ne peut pas être vide."
            )
        return value


class ResultatDiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultatDiagnostic
        fields = '__all__'

    def validate_score_confiance(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError(
                "Le score de confiance doit être compris entre 0 et 100."
            )
        return value

    def validate_rang(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Le rang doit être supérieur à 0."
            )
        return value


class RecommandationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommandation
        fields = '__all__'

    def validate_titre(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Le titre ne peut pas être vide."
            )
        return value


class MarcheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marche
        fields = '__all__'


class PrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prix
        fields = '__all__'

    def validate_prix(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Le prix ne peut pas être négatif."
            )
        return value


class ZoneMeteoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneMeteo
        fields = '__all__'


class PrevisionMeteoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrevisionMeteo
        fields = '__all__'

    def validate_humidite(self, value):
        if value is not None and (value < 0 or value > 100):
            raise serializers.ValidationError(
                "L'humidité doit être comprise entre 0 et 100."
            )
        return value

    def validate_probabilite_pluie(self, value):
        if value is not None and (value < 0 or value > 100):
            raise serializers.ValidationError(
                "La probabilité de pluie doit être comprise entre 0 et 100."
            )
        return value


class AnalyseDiagnosticSerializer(serializers.Serializer):
    symptomes = serializers.CharField(required=False, allow_blank=True)
    id_parcelle = serializers.IntegerField(required=False)
    id_maladie = serializers.IntegerField(required=False)
    numero_galerie = serializers.IntegerField(required=False)
    image = serializers.FileField(required=False)
