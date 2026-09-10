from django.core.management import call_command
from rest_framework.test import APITestCase


class AgriSenceAPITests(APITestCase):
    def setUp(self):
        call_command("seed_agrisence", verbosity=0)

    def test_sante(self):
        response = self.client.get("/api/sante/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["ok"])

    def test_connexion_agriculteur(self):
        response = self.client.post(
            "/api/auth/connexion/",
            {"telephone": "22961000001", "mot_de_passe": "tomate123"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["role"], "agriculteur")
        self.assertNotIn("mot_de_passe_hash", response.data)

    def test_connexion_refusee(self):
        response = self.client.post(
            "/api/auth/connexion/",
            {"telephone": "22961000001", "mot_de_passe": "mauvais"},
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_inscription_utilisateur(self):
        response = self.client.post(
            "/api/utilisateurs/",
            {
                "nom": "Bio",
                "prenom": "Chantal",
                "telephone": "22961000999",
                "email": "chantal@agrisence.bj",
                "role": "agriculteur",
                "mot_de_passe": "secret12",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["prenom"], "Chantal")

    def test_culture_unique(self):
        response = self.client.post(
            "/api/cultures/",
            {"nom": "Tomate", "description": "doublon"},
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_galerie(self):
        response = self.client.get("/api/maladies/galerie/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data["maladies"]), 7)

    def test_diagnostic_par_symptomes(self):
        response = self.client.post(
            "/api/diagnostics/analyse/",
            {
                "symptomes": "taches brunes, feuilles jaunes, moisissure blanche"
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data["resultats"])
        self.assertEqual(response.data["resultats"][0]["maladie"], "Mildiou")
        self.assertEqual(response.data["diagnostic"]["statut"], "termine")

    def test_diagnostic_galerie(self):
        response = self.client.post(
            "/api/diagnostics/analyse/",
            {"numero_galerie": 2},
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data["resultats"][0]["maladie"],
            "Alternariose",
        )

    def test_marches_et_prix(self):
        marches = self.client.get("/api/marches/")
        self.assertEqual(marches.status_code, 200)
        self.assertEqual(len(marches.data), 5)
        prix = self.client.get("/api/prix/")
        self.assertEqual(prix.status_code, 200)
        self.assertGreaterEqual(len(prix.data), 5)

    def test_meteo_risque(self):
        response = self.client.get("/api/previsions-meteo/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("risque_maladie_fongique", response.data[0])

    def test_conseils(self):
        response = self.client.get("/api/conseils/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 7)

    def test_agent_cas(self):
        self.client.post(
            "/api/diagnostics/analyse/",
            {"symptomes": "poudre blanche, feuilles qui se recroquevillent"},
            format="json",
        )
        response = self.client.get("/api/agent/cas/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_put_exploitation_renvoie_donnees(self):
        exploitations = self.client.get("/api/exploitations/")
        pk = exploitations.data[0]["id_exploitation"]
        response = self.client.put(
            f"/api/exploitations/{pk}/",
            {
                "nom": "Ferme Kouagou",
                "localisation": "Natitingou, Atacora",
                "superficie": "1.80",
                "id_utilisateur": exploitations.data[0]["id_utilisateur"],
            },
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["nom"], "Ferme Kouagou")
