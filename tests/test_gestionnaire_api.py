import sys
import os

# Ajouter le dossier `src/` au chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from gestionnaire_api import GestionnaireAPI


def test_get_stock_data():
    api = GestionnaireAPI()
    try:
        stock_data = api.get_stock_data("TSLA")
        assert isinstance(stock_data, list), "Les données doivent être une liste."
        assert "Date" in stock_data[0], "Chaque entrée doit contenir une clé 'Date'."
        print("Test `get_stock_data` réussi.")
    except Exception as e:
        print(f"Erreur dans `get_stock_data`: {e}")

def test_get_news():
    api = GestionnaireAPI()
    try:
        news_data = api.get_news("Tesla")
        assert isinstance(news_data, list), "Les données doivent être une liste."
        assert "Title" in news_data[0], "Chaque entrée doit contenir une clé 'Title'."
        print("Test `get_news` réussi.")
    except Exception as e:
        print(f"Erreur dans `get_news`: {e}")

if __name__ == "__main__":
    test_get_stock_data()
    test_get_news()
