import requests
import os
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

    def get_stock_data(self, symbol):
        """
        Récupère les données financières d'une entreprise via Alpha Vantage.
        :param symbol: Symbole boursier de l'entreprise (ex : TSLA)
        :return: Données JSON formatées pour le projet
        """
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.alpha_vantage_key
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if "Time Series (Daily)" not in data:
                raise Exception("Erreur : données introuvables.")
            return self._formater_donnees_financieres(data["Time Series (Daily)"])
        else:
            raise Exception(f"Erreur API Alpha Vantage : {response.status_code}")

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
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return self._formater_actualites(data["articles"])
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
