def calculer_largeur(donnees):
    """
    Calcule la largeur maximale de chaque colonne.
    Les clés du dictionnaire sont les en-têtes et les listes associées sont les données.
    """
    return {
        cle: max(len(cle), max(len(str(val)) for val in valeurs))
        for cle, valeurs in donnees.items()
    }


def afficher_entete(donnees, largeurs_colonnes):
    """
    Affiche l'en-tête du tableau en fonction des données et des largeurs de colonnes.
    """
    ligne_entete = " | ".join(
        f"{cle.ljust(largeurs_colonnes[cle])}" for cle in donnees.keys()
    )
    separateur = "-+-".join(
        "-" * largeurs_colonnes[cle] for cle in donnees.keys()
    )

    print(ligne_entete)
    print(separateur)


def afficher_ligne(donnees, largeurs_colonnes):
    """
    Affiche les lignes du tableau formaté avec les données.
    """
    nb_lignes = max(len(valeurs) for valeurs in donnees.values())

    for i in range(nb_lignes):
        ligne = " | ".join(
            f"{str(donnees[cle][i]).ljust(largeurs_colonnes[cle]) if i < len(donnees[cle]) else '':{largeurs_colonnes[cle]}}"
            for cle in donnees.keys()
        )
        print(ligne)


def afficher_tableau(donnees):
    """
    Fonction principale qui affiche le tableau en utilisant les fonctions de calcul et d'affichage.
    """
    # Calcul des largeurs de colonnes
    largeurs_colonnes = calculer_largeur(donnees)

    # Affichage de l'en-tête
    afficher_entete(donnees, largeurs_colonnes)

    # Affichage des lignes de données
    afficher_ligne(donnees, largeurs_colonnes)


def main():
    """
    Fonction principale pour tester l'affichage du tableau à partir de données.
    """
    # Exemple de données
    donnees = {
        "Nom": ["Alice", "Bob", "Charlie", "Guido", "Thierry"],
        "Âge": [25, 30, 22, 60, 47],
        "Ville": ["Paris", "Lyon", "Marseille", "Boston", "Fribourg"],
    }

    # Afficher le tableau en appelant la fonction principale
    print("Tableau affiché :\n")
    afficher_tableau(donnees)

    # Vérification manuelle des largeurs des colonnes
    largeurs_attendues = {
        "Nom": 7,  # "Thierry" est le plus long avec 7 caractères
        "Âge": 3,  # "Âge" est le plus long avec 3 caractères
        "Ville": 9,  # "Fribourg" est le plus long avec 9 caractères
    }

    largeurs_colonnes = calculer_largeur(donnees)
    assert (
        largeurs_colonnes == largeurs_attendues
    ), f"Erreur dans les largeurs: {largeurs_colonnes}"

    print("\nTest de calcul des largeurs des colonnes réussi.\n")

    # Afficher l'en-tête et une ligne pour vérifier le bon fonctionnement
    print("Affichage de l'en-tête :")
    afficher_entete(donnees, largeurs_colonnes)

    print("\nAffichage de la première ligne de données :")
    afficher_ligne(donnees, largeurs_colonnes)

    print("\nTous les tests ont réussi.")


# Appel de la fonction main pour exécuter les tests
if __name__ == "__main__":
    main()
