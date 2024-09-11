def get_user_name():
    """
    Fonction pour obtenir et valider le nom de l'utilisateur.
    Retourne le nom s'il est valide (contient uniquement des caractères alphabétiques).
    """
    while True:
        name = input("Veuillez entrer votre nom : ")
        if name.isalpha():
            return name
        else:
            print(
                "Saisie invalide. Le nom doit uniquement contenir des lettres."
            )


def get_user_age():
    """
    Fonction pour obtenir et valider l'âge de l'utilisateur.
    Retourne l'âge en tant qu'entier s'il est valide (nombre entier positif).
    """
    while True:
        age_input = input("Veuillez entrer votre âge : ")
        try:
            age = int(age_input)
            if age <= 0:
                raise ValueError
            return age
        except ValueError:
            print("Saisie invalide. L'âge doit être un entier positif.")


def get_user_email():
    """
    Fonction pour obtenir et valider l'adresse email de l'utilisateur.
    Retourne l'email si celui-ci est valide (contient un "@" et un domaine valide).
    """
    while True:
        email = input("Veuillez entrer votre adresse email : ")
        if "@" in email and "." in email.split("@")[-1]:
            return email
        else:
            print(
                "Format d'email invalide. Veuillez entrer une adresse email valide."
            )


def get_user_info():
    """
    Fonction principale qui appelle les sous-fonctions pour obtenir et valider le nom,
    l'âge et l'email de l'utilisateur. Renvoie les informations collectées sous forme de dictionnaire.
    """
    name = get_user_name()
    age = get_user_age()
    email = get_user_email()

    print(
        f"Merci, {name}. Vous avez {age} ans et votre adresse email est {email}."
    )

    return {"name": name, "age": age, "email": email}


def main():
    """
    Fonction principale pour démontrer le bon fonctionnement du programme.
    Appelle la fonction get_user_info() et affiche les informations retournées.
    """
    # Appel de la fonction pour obtenir les informations de l'utilisateur
    user_info = get_user_info()

    # Affichage du dictionnaire contenant les informations de l'utilisateur
    print("\nInformations de l'utilisateur :")
    print(f"Nom : {user_info['name']}")
    print(f"Âge : {user_info['age']}")
    print(f"Email : {user_info['email']}")


# Protection pour éviter l'exécution lors d'un import
if __name__ == "__main__":
    main()
