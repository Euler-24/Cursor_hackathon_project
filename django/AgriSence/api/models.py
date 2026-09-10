
from django.conf import settings
from django.db import models


class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=150, unique=True, null=True, blank=True)
    mot_de_passe_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=30)
    date_inscription = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "utilisateur"
        managed = getattr(settings, "TESTING", False)


class Exploitation(models.Model):
    id_exploitation = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=150)
    localisation = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    superficie = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    id_utilisateur = models.ForeignKey(
        Utilisateur,
        on_delete=models.DO_NOTHING,
        db_column="id_utilisateur"
    )

    class Meta:
        db_table = "exploitation"
        managed = getattr(settings, "TESTING", False)


class Culture(models.Model):
    id_culture = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "culture"
        managed = getattr(settings, "TESTING", False)


class Parcelle(models.Model):
    id_parcelle = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    superficie = models.DecimalField(max_digits=10, decimal_places=2)
    date_plantation = models.DateField(null=True, blank=True)

    id_exploitation = models.ForeignKey(
        Exploitation,
        on_delete=models.DO_NOTHING,
        db_column="id_exploitation"
    )

    id_culture = models.ForeignKey(
        Culture,
        on_delete=models.DO_NOTHING,
        db_column="id_culture"
    )

    class Meta:
        db_table = "parcelle"
        managed = getattr(settings, "TESTING", False)


class Maladie(models.Model):
    id_maladie = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=150, unique=True)
    description_maladie = models.TextField(null=True, blank=True)
    symptomes = models.TextField(null=True, blank=True)
    gravite = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = "maladie"
        managed = getattr(settings, "TESTING", False)


class Diagnostic(models.Model):
    id_diagnostic = models.AutoField(primary_key=True)
    date_diagnostic = models.DateTimeField()
    url_image = models.CharField(max_length=500, null=True, blank=True)
    description_symptomes = models.TextField(null=True, blank=True)
    statut = models.CharField(max_length=30)

    id_parcelle = models.ForeignKey(
        Parcelle,
        on_delete=models.DO_NOTHING,
        db_column="id_parcelle"
    )

    class Meta:
        db_table = "diagnostic"
        managed = getattr(settings, "TESTING", False)


class ResultatDiagnostic(models.Model):
    id_resultat = models.AutoField(primary_key=True)

    id_diagnostic = models.ForeignKey(
        Diagnostic,
        on_delete=models.DO_NOTHING,
        db_column="id_diagnostic"
    )

    id_maladie = models.ForeignKey(
        Maladie,
        on_delete=models.DO_NOTHING,
        db_column="id_maladie"
    )

    score_confiance = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    rang = models.PositiveSmallIntegerField()

    est_retenu = models.BooleanField(default=False)

    class Meta:
        db_table = "resultat_diagnostic"
        managed = getattr(settings, "TESTING", False)


class Recommandation(models.Model):
    id_recommandation = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    niveau_urgence = models.CharField(max_length=30, null=True, blank=True)

    id_maladie = models.ForeignKey(
        Maladie,
        on_delete=models.DO_NOTHING,
        db_column="id_maladie"
    )

    class Meta:
        db_table = "recommandation"
        managed = getattr(settings, "TESTING", False)


class Marche(models.Model):
    id_marche = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=150)
    localisation = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)

    class Meta:
        db_table = "marche"
        managed = getattr(settings, "TESTING", False)


class Prix(models.Model):
    id_prix = models.AutoField(primary_key=True)
    prix = models.DecimalField(max_digits=12, decimal_places=2)
    unite = models.CharField(max_length=50)
    devise = models.CharField(max_length=10)
    date_releve = models.DateField()
    source = models.CharField(max_length=255, null=True, blank=True)

    id_marche = models.ForeignKey(
        Marche,
        on_delete=models.DO_NOTHING,
        db_column="id_marche"
    )

    id_culture = models.ForeignKey(
        Culture,
        on_delete=models.DO_NOTHING,
        db_column="id_culture"
    )

    class Meta:
        db_table = "prix"
        managed = getattr(settings, "TESTING", False)


class ZoneMeteo(models.Model):
    id_zone = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=150)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)

    class Meta:
        db_table = "zone_meteo"
        managed = getattr(settings, "TESTING", False)


class PrevisionMeteo(models.Model):
    id_prevision = models.AutoField(primary_key=True)
    date_prevision = models.DateField()
    temperature_min = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    temperature_max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    humidite = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    probabilite_pluie = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    quantite_pluie = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    id_zone = models.ForeignKey(
        ZoneMeteo,
        on_delete=models.DO_NOTHING,
        db_column="id_zone"
    )

    class Meta:
        db_table = "prevision_meteo"
        managed = getattr(settings, "TESTING", False)
