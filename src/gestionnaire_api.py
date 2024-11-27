import requests
import os
import time
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

class GestionnaireAPI:
    def __init__(self):
        """
        Initialise les clés API nécessaires pour Alpha Vantage et News API.
        """
        self.alpha_vantage_key = os.getenv("ALPHA_VANTAGE_KEY")
        self.news_api_key = os.getenv("NEWS_API_KEY")

    def collecter_donnees_entreprises(self, entreprises):
        """
        Collecte les données financières et les actualités pour plusieurs entreprises.
        :param entreprises: Dictionnaire des entreprises à traiter.
        :return: Dictionnaire contenant les données collectées.
        """
        donnees_financieres = {}
        actualites = {}

        for symbole, info in entreprises.items():
            try:
                donnees_financieres[symbole] = self.get_stock_data(symbole)
                actualites[symbole] = self.get_news(info["nom"])
                print(f"Collecte réussie pour {info['nom']} ({symbole})")
            except Exception as e:
                print(f"Erreur pour {info['nom']} ({symbole}): {e}")

        return donnees_financieres, actualites

    def get_stock_data(self, symbol, max_retries=5):
        retry_count = 0
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.alpha_vantage_key
        }
        while retry_count < max_retries:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                if "Time Series (Daily)" in data:
                    return self._formater_donnees_financieres(data["Time Series (Daily)"])
                elif "Note" in data:
                    print(f"Rate limit atteint pour {symbol}. Attente...")
                    time.sleep(60)
                    retry_count += 1
                else:
                    raise Exception(f"Erreur : données introuvables pour {symbol}.")
            elif response.status_code == 429:
                print(f"Rate limit HTTP 429 pour {symbol}. Réessai...")
                time.sleep(60)
                retry_count += 1
            else:
                raise Exception(f"Erreur API Alpha Vantage ({response.status_code}) pour {symbol}")
        raise Exception(f"Échec après {max_retries} tentatives pour {symbol}")

    def _formater_donnees_financieres(self, donnees_brutes):
        """
        Formate les données brutes en une liste exploitable.
        :param donnees_brutes: Données brutes issues de l'API Alpha Vantage
        :return: Liste de dictionnaires formatés
        """
        donnees_formattees = []
        for date, valeurs in donnees_brutes.items():
            donnees_formattees.append({
                "Date": date,
                "Open": float(valeurs["1. open"]),
                "High": float(valeurs["2. high"]),
                "Low": float(valeurs["3. low"]),
                "Close": float(valeurs["4. close"]),
                "Volume": int(valeurs["5. volume"])
            })
        return donnees_formattees

    def get_news(self, query):
        """
        Récupère les actualités pour une entreprise donnée via News API.
        :param query: Nom ou mot-clé de l'entreprise (ex : Tesla)
        :return: Liste d'articles pertinents
        """
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": query,
            "sortBy": "relevancy",
            "language": "en",
            "apiKey": self.news_api_key
        }

        while True:  # Boucle pour réessayer en cas de dépassement de quota
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                return self._formater_actualites(data["articles"])
            elif response.status_code == 429:  # Code HTTP pour trop de requêtes
                print("Rate limit atteint (HTTP 429). Attente en cours...")
                time.sleep(60)  # Attendre 1 minute avant de réessayer
            else:
                raise Exception(f"Erreur API News API : {response.status_code}")

    def _formater_actualites(self, articles_bruts):
        """
        Formate les articles bruts en une liste exploitable.
        :param articles_bruts: Données brutes issues de l'API News API
        :return: Liste de dictionnaires formatés
        """
        articles_formattees = []
        for article in articles_bruts:
            articles_formattees.append({
                "Title": article.get("title", "N/A"),
                "Author": article.get("author", "N/A"),
                "PublishedAt": article.get("publishedAt", "N/A"),
                "Description": article.get("description", "N/A"),
                "URL": article.get("url", "N/A")
            })
        return articles_formattees
