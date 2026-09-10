import requests

BASE = "http://127.0.0.1:8000/api"

print("Santé:", requests.get(f"{BASE}/sante/").status_code)

login = requests.post(
    f"{BASE}/auth/connexion/",
    json={"telephone": "22961000001", "mot_de_passe": "tomate123"},
)
print("Connexion:", login.status_code, login.json().get("prenom"))

diag = requests.post(
    f"{BASE}/diagnostics/analyse/",
    json={"symptomes": "taches brunes, feuilles jaunes"},
)
print("Diagnostic:", diag.status_code)
if diag.ok:
    print("  ->", diag.json()["resultats"][0]["maladie"])

print("Marchés:", requests.get(f"{BASE}/marches/").status_code)
print("Météo:", requests.get(f"{BASE}/previsions-meteo/").status_code)
print("Conseils:", requests.get(f"{BASE}/conseils/").status_code)
