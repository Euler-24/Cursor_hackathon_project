"""Base de connaissances AgriSense Tomato (Atacora)."""

MALADIES_TOMATE = {
    "Mildiou": {
        "symptomes": [
            "taches brunes",
            "feuilles jaunes",
            "moisissure blanche sous la feuille",
            "tiges noircies",
        ],
        "cause": (
            "Champignon (Phytophthora infestans), favorisé par "
            "l'humidité et la fraîcheur"
        ),
        "conseil": (
            "Retirer et brûler les feuilles atteintes, espacer les plants, "
            "éviter d'arroser le feuillage, traiter au cuivre"
        ),
        "gravite": "elevee",
        "photo_reference": "photos/mildiou.jpg",
        "mots_image": ["mildiou", "lateblight", "late-blight", "phytophthora"],
    },
    "Alternariose": {
        "symptomes": [
            "taches noires concentriques",
            "feuilles qui jaunissent",
            "fruits taches",
            "chute des feuilles basses",
        ],
        "cause": (
            "Champignon (Alternaria solani), favorisé par la chaleur "
            "et l'humidité alternées"
        ),
        "conseil": (
            "Enlever les feuilles infectées, améliorer l'aération "
            "entre les plants, rotation des cultures"
        ),
        "gravite": "moyenne",
        "photo_reference": "photos/alternariose.jpg",
        "mots_image": ["alternaria", "earlyblight", "early-blight"],
    },
    "Fusariose": {
        "symptomes": [
            "jaunissement d'un seul cote de la plante",
            "fletrissement",
            "tige brune a l'interieur",
        ],
        "cause": (
            "Champignon du sol (Fusarium oxysporum), qui bloque "
            "la circulation de l'eau"
        ),
        "conseil": (
            "Arracher et détruire les plants atteints, ne pas replanter "
            "de tomates au même endroit"
        ),
        "gravite": "elevee",
        "photo_reference": "photos/fusariose.jpg",
        "mots_image": ["fusarium", "fusariose", "wilt"],
    },
    "Oidium": {
        "symptomes": [
            "poudre blanche sur les feuilles",
            "feuilles qui se recroquevillent",
            "croissance ralentie",
        ],
        "cause": (
            "Champignon favorisé par un temps sec et chaud "
            "avec humidité nocturne"
        ),
        "conseil": (
            "Améliorer la circulation de l'air, éviter l'excès "
            "d'engrais azoté, traiter au soufre"
        ),
        "gravite": "moyenne",
        "photo_reference": "photos/oidium.jpg",
        "mots_image": ["oidium", "powdery", "mildew"],
    },
    "Pourriture apicale": {
        "symptomes": [
            "tache noire et molle au bout du fruit",
            "fruit qui pourrit par le bas",
        ],
        "cause": "Carence en calcium, souvent liée à un arrosage irrégulier",
        "conseil": (
            "Arroser régulièrement et de façon constante, "
            "apporter du calcium au sol"
        ),
        "gravite": "moyenne",
        "photo_reference": "photos/pourriture_apicale.jpg",
        "mots_image": ["blossom", "apicale", "calcium"],
    },
    "Carence en azote": {
        "symptomes": [
            "feuilles jaunes uniformes",
            "croissance lente",
            "tige fine et pale",
        ],
        "cause": "Manque d'azote disponible dans le sol",
        "conseil": (
            "Apporter un engrais riche en azote ou du compost "
            "bien décomposé"
        ),
        "gravite": "faible",
        "photo_reference": "photos/carence_azote.jpg",
        "mots_image": ["azote", "nitrogen", "jaune"],
    },
    "Acariens": {
        "symptomes": [
            "petits points jaunes sur les feuilles",
            "toiles fines sous les feuilles",
            "feuilles qui se dessechent",
        ],
        "cause": "Parasite (acarien), favorisé par la chaleur et la sécheresse",
        "conseil": (
            "Augmenter l'humidité ambiante, pulvériser de l'eau "
            "sur les feuilles, savon insecticide si besoin"
        ),
        "gravite": "moyenne",
        "photo_reference": "photos/acariens.jpg",
        "mots_image": ["acarien", "spider", "mite"],
    },
}


def _normaliser(texte):
    if not texte:
        return ""
    return (
        str(texte)
        .strip()
        .lower()
        .replace("é", "e")
        .replace("è", "e")
        .replace("ê", "e")
        .replace("à", "a")
        .replace("ù", "u")
        .replace("ô", "o")
        .replace("ç", "c")
    )


def diagnostiquer_par_symptomes(symptomes_observes, seuil_minimum=0.3):
    observes = [_normaliser(s) for s in symptomes_observes if str(s).strip()]
    resultats = []

    for nom_maladie, infos in MALADIES_TOMATE.items():
        refs = [_normaliser(s) for s in infos["symptomes"]]
        correspondances = 0
        for observe in observes:
            for ref in refs:
                if observe in ref or ref in observe:
                    correspondances += 1
                    break
        taux = correspondances / len(refs) if refs else 0
        resultats.append((nom_maladie, taux, infos))

    resultats.sort(key=lambda x: x[1], reverse=True)
    return [r for r in resultats if r[1] >= seuil_minimum]


def diagnostiquer_par_nom_fichier(nom_fichier):
    nom = _normaliser(nom_fichier)
    for maladie, infos in MALADIES_TOMATE.items():
        for mot in infos["mots_image"]:
            if mot in nom:
                return maladie, infos
    return None, None


def galerie():
    items = []
    for i, (nom, infos) in enumerate(MALADIES_TOMATE.items(), start=1):
        items.append({
            "numero": i,
            "nom": nom,
            "photo_reference": infos["photo_reference"],
            "symptomes": infos["symptomes"],
            "gravite": infos["gravite"],
        })
    return items
