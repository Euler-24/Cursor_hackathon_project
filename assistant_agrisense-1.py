# ================================================================
# AGRISENSE TOMATO - ASSISTANT DE DIAGNOSTIC (version interlocuteur)
# Auteur : Rebecca - Traitement de données & analyse intelligente
# ================================================================
#
# BUT DU PROGRAMME :
# Cet assistant dialogue avec le producteur pour identifier la
# maladie de sa plante de tomate, de 3 façons possibles :
#
#   CHEMIN C - il décrit les symptômes qu'il observe (texte)
#   CHEMIN B - il regarde une galerie de photos de référence et
#              choisit celle qui ressemble à sa plante
#   CHEMIN A - il envoie une photo de sa plante et l'IA la reconnaît
#              automatiquement (PREVU pour la Phase 2, dataset
#              PlantVillage + modèle de reconnaissance d'image)
#
# Ce script est la "logique" (le cerveau). L'interface graphique
# (les boutons, l'écran) sera construite par Mariano/Augustin.
# Ici, on simule la conversation dans la console pour valider
# que la logique fonctionne avant de la brancher à l'app.
# ================================================================


# ================================================================
# BASE DE CONNAISSANCES : LES MALADIES DE LA TOMATE
# ================================================================
# Chaque maladie a maintenant un champ "photo_reference" en plus :
# c'est le nom du fichier image qui la représente (viendra du
# dataset PlantVillage une fois téléchargé).

maladies = {
    "Mildiou": {
        "symptomes": ["taches brunes", "feuilles jaunes", "moisissure blanche sous la feuille", "tiges noircies"],
        "cause": "Champignon (Phytophthora infestans), favorisé par l'humidité et la fraîcheur",
        "conseil": "Retirer et brûler les feuilles atteintes, espacer les plants, éviter d'arroser le feuillage, traiter au cuivre",
        "photo_reference": "photos/mildiou.jpg"
    },
    "Alternariose": {
        "symptomes": ["taches noires concentriques", "feuilles qui jaunissent", "fruits tachés", "chute des feuilles basses"],
        "cause": "Champignon (Alternaria solani), favorisé par la chaleur et l'humidité alternées",
        "conseil": "Enlever les feuilles infectées, améliorer l'aération entre les plants, rotation des cultures",
        "photo_reference": "photos/alternariose.jpg"
    },
    "Fusariose": {
        "symptomes": ["jaunissement d'un seul côté de la plante", "flétrissement", "tige brune à l'intérieur"],
        "cause": "Champignon du sol (Fusarium oxysporum), qui bloque la circulation de l'eau",
        "conseil": "Arracher et détruire les plants atteints, ne pas replanter de tomates au même endroit",
        "photo_reference": "photos/fusariose.jpg"
    },
    "Oidium": {
        "symptomes": ["poudre blanche sur les feuilles", "feuilles qui se recroquevillent", "croissance ralentie"],
        "cause": "Champignon favorisé par un temps sec et chaud avec humidité nocturne",
        "conseil": "Améliorer la circulation de l'air, éviter l'excès d'engrais azoté, traiter au soufre",
        "photo_reference": "photos/oidium.jpg"
    },
    "Pourriture apicale": {
        "symptomes": ["tache noire et molle au bout du fruit", "fruit qui pourrit par le bas"],
        "cause": "Carence en calcium, souvent liée à un arrosage irrégulier",
        "conseil": "Arroser régulièrement et de façon constante, apporter du calcium au sol",
        "photo_reference": "photos/pourriture_apicale.jpg"
    },
    "Carence en azote": {
        "symptomes": ["feuilles jaunes uniformes", "croissance lente", "tige fine et pâle"],
        "cause": "Manque d'azote disponible dans le sol",
        "conseil": "Apporter un engrais riche en azote ou du compost bien décomposé",
        "photo_reference": "photos/carence_azote.jpg"
    },
    "Acariens": {
        "symptomes": ["petits points jaunes sur les feuilles", "toiles fines sous les feuilles", "feuilles qui se dessèchent"],
        "cause": "Parasite (acarien), favorisé par la chaleur et la sécheresse",
        "conseil": "Augmenter l'humidité ambiante, pulvériser de l'eau sur les feuilles, savon insecticide si besoin",
        "photo_reference": "photos/acariens.jpg"
    },
}


# ================================================================
# CHEMIN C : DIAGNOSTIC PAR DESCRIPTION DE SYMPTOMES
# ================================================================
def diagnostiquer_par_symptomes(symptomes_observes, seuil_minimum=0.3):
    """
    Compare les symptômes décrits par l'utilisateur avec chaque
    maladie, et retourne celles dont le taux de correspondance
    dépasse le seuil minimum (30% par défaut).
    """
    resultats = []

    for nom_maladie, infos in maladies.items():
        correspondances = sum(1 for s in symptomes_observes if s in infos["symptomes"])
        taux = correspondances / len(infos["symptomes"])
        resultats.append((nom_maladie, taux))

    resultats.sort(key=lambda x: x[1], reverse=True)
    return [r for r in resultats if r[1] >= seuil_minimum]


# ================================================================
# CHEMIN B : DIAGNOSTIC PAR GALERIE DE PHOTOS (choix manuel)
# ================================================================
def afficher_galerie():
    """
    Affiche la liste des maladies avec leur photo de référence,
    numérotées, pour que l'utilisateur choisisse celle qui
    ressemble à sa plante.
    """
    print("\nVoici les maladies les plus courantes. Regardez les photos et choisissez celle qui ressemble à votre plante :\n")

    liste_maladies = list(maladies.keys())  # on transforme les noms en liste numérotable

    for i, nom in enumerate(liste_maladies, start=1):
        print(f"{i}. {nom}  (photo : {maladies[nom]['photo_reference']})")

    return liste_maladies


def diagnostic_par_choix(numero_choisi, liste_maladies):
    """
    Une fois que l'utilisateur a choisi un numéro dans la galerie,
    cette fonction retourne directement la maladie correspondante.
    Pas besoin de calcul de score ici : l'utilisateur a confirmé
    visuellement lui-même.
    """
    index = numero_choisi - 1  # on ajuste car les listes commencent à 0 en Python
    if 0 <= index < len(liste_maladies):
        return liste_maladies[index]
    return None


# ================================================================
# CHEMIN A : EMPLACEMENT PREVU POUR L'IA DE RECONNAISSANCE D'IMAGE
# ================================================================
def diagnostiquer_par_photo_ia(chemin_photo_utilisateur):
    """
    ⚠️ PHASE 2 - PAS ENCORE IMPLEMENTE ⚠️

    Cette fonction est prête à recevoir une vraie photo envoyée par
    l'utilisateur et à la comparer automatiquement avec le modèle
    entraîné sur le dataset PlantVillage.

    Pour l'instant, elle renvoie un message clair indiquant que
    cette fonctionnalité arrive, et redirige vers le Chemin B
    (galerie) en attendant.
    """
    print("\nLa reconnaissance automatique de photo par IA n'est pas encore activée.")
    print("En attendant, voici la galerie pour identifier votre plante manuellement :")
    return afficher_galerie()


# ================================================================
# AFFICHAGE D'UN DIAGNOSTIC FINAL (commun aux 3 chemins)
# ================================================================
def afficher_resultat(nom_maladie, taux=None):
    """
    Affiche le résultat final de façon lisible pour l'agriculteur,
    peu importe le chemin par lequel on est arrivé au diagnostic.
    """
    infos = maladies[nom_maladie]
    print(f"\n🍅 Diagnostic : {nom_maladie}")
    if taux is not None:
        print(f"   Fiabilité estimée : {round(taux * 100)}%")
    print(f"   Cause : {infos['cause']}")
    print(f"   Conseil : {infos['conseil']}\n")


# ================================================================
# L'ASSISTANT - BOUCLE DE CONVERSATION PRINCIPALE
# ================================================================
def assistant_agrisense():
    """
    C'est le coeur de l'assistant : il accueille l'utilisateur,
    lui propose ses options, et l'oriente vers le bon chemin
    de diagnostic selon son choix.
    """
    print("=" * 50)
    print("Bonjour, je suis votre assistant AgriSense 🍅")
    print("Je vais vous aider à diagnostiquer votre plant de tomate.")
    print("=" * 50)

    print("\nComment souhaitez-vous procéder ?")
    print("1. Décrire les symptômes que je vois sur ma plante")
    print("2. Regarder une galerie de photos pour reconnaître le problème")
    print("3. Envoyer une photo de ma plante (fonctionnalité à venir)")

    choix = input("\nVotre choix (1, 2 ou 3) : ")

    # ----- CHEMIN C : description texte -----
    if choix == "1":
        print("\nDécrivez vos symptômes séparés par une virgule.")
        print("Exemple : taches brunes, feuilles jaunes")
        entree = input("Vos symptômes : ")
        symptomes_utilisateur = [s.strip() for s in entree.split(",")]

        resultats = diagnostiquer_par_symptomes(symptomes_utilisateur)
        if not resultats:
            print("\nJe n'ai pas identifié de maladie fiable avec ces symptômes. Essayez d'en décrire d'autres, ou consultez un agent agricole.")
        else:
            for nom_maladie, taux in resultats:
                afficher_resultat(nom_maladie, taux)

    # ----- CHEMIN B : galerie photo -----
    elif choix == "2":
        liste_maladies = afficher_galerie()
        numero = int(input("\nEntrez le numéro correspondant à votre plante : "))
        maladie_trouvee = diagnostic_par_choix(numero, liste_maladies)

        if maladie_trouvee:
            afficher_resultat(maladie_trouvee)
        else:
            print("\nNuméro invalide, veuillez réessayer.")

    # ----- CHEMIN A : photo IA (pas encore prêt) -----
    elif choix == "3":
        diagnostiquer_par_photo_ia("chemin_de_la_photo_envoyee.jpg")

    else:
        print("\nChoix non reconnu. Veuillez relancer l'assistant.")


# ================================================================
# LANCEMENT DE L'ASSISTANT
# ================================================================
if __name__ == "__main__":
    assistant_agrisense()
