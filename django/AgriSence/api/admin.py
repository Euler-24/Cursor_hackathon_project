from django.contrib import admin
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


@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ("id_utilisateur", "nom", "prenom", "telephone", "role")
    search_fields = ("nom", "prenom", "telephone", "email")


@admin.register(Exploitation)
class ExploitationAdmin(admin.ModelAdmin):
    list_display = ("id_exploitation", "nom", "localisation", "id_utilisateur")


@admin.register(Parcelle)
class ParcelleAdmin(admin.ModelAdmin):
    list_display = ("id_parcelle", "nom", "id_exploitation", "id_culture")


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = ("id_culture", "nom")


@admin.register(Maladie)
class MaladieAdmin(admin.ModelAdmin):
    list_display = ("id_maladie", "nom", "gravite")


@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ("id_diagnostic", "statut", "date_diagnostic", "id_parcelle")


@admin.register(ResultatDiagnostic)
class ResultatDiagnosticAdmin(admin.ModelAdmin):
    list_display = (
        "id_resultat",
        "id_diagnostic",
        "id_maladie",
        "score_confiance",
        "est_retenu",
    )


@admin.register(Recommandation)
class RecommandationAdmin(admin.ModelAdmin):
    list_display = ("id_recommandation", "titre", "niveau_urgence", "id_maladie")


@admin.register(Marche)
class MarcheAdmin(admin.ModelAdmin):
    list_display = ("id_marche", "nom", "localisation")


@admin.register(Prix)
class PrixAdmin(admin.ModelAdmin):
    list_display = ("id_prix", "prix", "devise", "date_releve", "id_marche")


@admin.register(ZoneMeteo)
class ZoneMeteoAdmin(admin.ModelAdmin):
    list_display = ("id_zone", "nom")


@admin.register(PrevisionMeteo)
class PrevisionMeteoAdmin(admin.ModelAdmin):
    list_display = ("id_prevision", "date_prevision", "id_zone")
