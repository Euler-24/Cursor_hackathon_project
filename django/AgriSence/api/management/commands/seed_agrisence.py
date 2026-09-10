from datetime import date, timedelta

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from django.utils import timezone

from api.knowledge import MALADIES_TOMATE
from api.models import (
    Culture,
    Exploitation,
    Marche,
    Parcelle,
    PrevisionMeteo,
    Prix,
    Utilisateur,
    ZoneMeteo,
)
from api.tomato_views import _assurer_maladie


class Command(BaseCommand):
    help = "Charge les données de démonstration AgriSense Tomato (Atacora)."

    def handle(self, *args, **options):
        agriculteur, _ = Utilisateur.objects.get_or_create(
            telephone="22961000001",
            defaults={
                "nom": "Kouagou",
                "prenom": "Pierre",
                "email": "pierre.kouagou@agrisence.bj",
                "mot_de_passe_hash": make_password("tomate123"),
                "role": "agriculteur",
                "date_inscription": timezone.now(),
            },
        )
        Utilisateur.objects.get_or_create(
            telephone="22961000002",
            defaults={
                "nom": "Sabi",
                "prenom": "Amina",
                "email": "amina.sabi@agrisence.bj",
                "mot_de_passe_hash": make_password("agent123"),
                "role": "agent agricole",
                "date_inscription": timezone.now(),
            },
        )

        culture, _ = Culture.objects.get_or_create(
            nom="Tomate",
            defaults={
                "description": "Culture principale suivie par AgriSense Tomato."
            },
        )

        exploitation, _ = Exploitation.objects.get_or_create(
            nom="Ferme Kouagou",
            id_utilisateur=agriculteur,
            defaults={
                "localisation": "Natitingou, Atacora",
                "latitude": 10.3042,
                "longitude": 1.3796,
                "superficie": 1.50,
            },
        )
        Parcelle.objects.get_or_create(
            nom="Parcelle tomate 1",
            id_exploitation=exploitation,
            defaults={
                "superficie": 0.40,
                "date_plantation": date.today() - timedelta(days=40),
                "id_culture": culture,
            },
        )

        for nom, infos in MALADIES_TOMATE.items():
            _assurer_maladie(nom, infos)

        marches = [
            ("Marché de Natitingou", "Natitingou", 10.3042, 1.3796, 850),
            ("Marché de Tanguiéta", "Tanguiéta", 10.6211, 1.2664, 800),
            ("Marché de Toucountouna", "Toucountouna", 10.4660, 1.3700, 780),
            ("Marché de Kouandé", "Kouandé", 10.3317, 1.6914, 820),
            ("Marché de Matéri", "Matéri", 10.8170, 1.0110, 760),
        ]
        for nom, loc, lat, lng, prix in marches:
            marche, _ = Marche.objects.get_or_create(
                nom=nom,
                defaults={
                    "localisation": loc,
                    "latitude": lat,
                    "longitude": lng,
                },
            )
            Prix.objects.get_or_create(
                id_marche=marche,
                id_culture=culture,
                date_releve=date.today(),
                defaults={
                    "prix": prix,
                    "unite": "kg",
                    "devise": "XOF",
                    "source": "Relevé Atacora (indicatif)",
                },
            )

        zone, _ = ZoneMeteo.objects.get_or_create(
            nom="Natitingou",
            defaults={"latitude": 10.3042, "longitude": 1.3796},
        )
        for i in range(5):
            PrevisionMeteo.objects.get_or_create(
                id_zone=zone,
                date_prevision=date.today() + timedelta(days=i),
                defaults={
                    "temperature_min": 22 + i * 0.3,
                    "temperature_max": 32 + i * 0.2,
                    "humidite": 70 + i,
                    "probabilite_pluie": 35 + i * 5,
                    "quantite_pluie": 4 + i,
                },
            )

        self.stdout.write(self.style.SUCCESS(
            "Données de démo prêtes. "
            "Agriculteur 22961000001 / tomate123 — "
            "Agent 22961000002 / agent123"
        ))
