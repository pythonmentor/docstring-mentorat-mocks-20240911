import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def extract_titles_from_html(html_content):
    """
    Extrait les titres des articles à partir du contenu HTML d'une page.

    Args:
        html_content (str): Le contenu HTML de la page.

    Returns:
        list: Une liste de titres des articles.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    titles = []

    # Recherche la section qui contient les articles
    articles_section = soup.find("div", class_="colonneActu")
    if articles_section:
        # Trouve toutes les balises <a> avec la classe 'titre' qui contiennent les titres
        for article in articles_section.find_all("a", class_="titre"):
            title = article.get_text(strip=True)
            titles.append(title)

    return titles


def get_next_page_url(html_content):
    """
    Extrait l'URL de la page suivante à partir du contenu HTML, si elle existe.

    Args:
        html_content (str): Le contenu HTML de la page.

    Returns:
        str or None: L'URL de la page suivante, ou None s'il n'y a pas de page suivante.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    pagination = soup.find("div", class_="pagination")

    if pagination:
        # Recherche du lien "Page suivante" (indiqué par l'icône 'fa-angle-right' dans l'exemple)
        next_page_link = pagination.find("a", title="Page suivante")
        if next_page_link and "href" in next_page_link.attrs:
            return next_page_link["href"]

    return None


def get_all_titles(base_url="https://python.developpez.com"):
    """
    Récupère tous les titres des articles du site python.developpez.com en parcourant les pages dynamiquement.

    Args:
        base_url (str): L'URL de base des articles de python.developpez.com.

    Returns:
        list: Une liste de tous les titres des articles récupérés.
    """
    titles = []
    current_page_url = base_url
    visited_pages = (
        set()
    )  # Pour éviter les boucles infinies si une page est revisitée

    try:
        while current_page_url and current_page_url not in visited_pages:
            print(f"Fetching articles from: {current_page_url}")
            visited_pages.add(
                current_page_url
            )  # Marquer cette page comme visitée

            response = requests.get(current_page_url, timeout=5)

            if response.status_code != 200:
                print(
                    f"Erreur : échec de la récupération de la page (code HTTP {response.status_code})"
                )
                continue

            # Extraire les titres à partir du contenu HTML de la page
            page_titles = extract_titles_from_html(response.content)
            if not page_titles:
                print(f"Aucun titre trouvé sur la page {current_page_url}")
                break

            titles.extend(page_titles)

            # Trouver l'URL de la page suivante
            next_page_url = get_next_page_url(response.content)
            if next_page_url:
                current_page_url = (
                    base_url + next_page_url
                )  # Construire l'URL complète pour la prochaine page
            else:
                print("Pas de page suivante trouvée, fin de la pagination.")
                break

    except RequestException as e:
        print(
            f"Erreur de connexion : impossible de joindre le site ({str(e)})"
        )

    return titles


def main():
    """
    Fonction principale pour exécuter le script et récupérer les titres.
    """
    # Appeler la fonction pour récupérer tous les titres
    all_titles = get_all_titles()

    # Afficher tous les titres récupérés
    if all_titles:
        for idx, title in enumerate(all_titles, 1):
            print(f"{idx}. {title}")
    else:
        print("Aucun titre n'a été trouvé.")


# Exécuter la fonction main si ce script est exécuté directement
if __name__ == "__main__":
    main()
