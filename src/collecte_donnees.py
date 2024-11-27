from gestionnaire_api import GestionnaireAPI
from gestionnaire_fichier import GestionnaireFichier
from gestionnaire_logs import logger

NOMS_ENTREPRISES = {
    "TSLA": {"nom": "Tesla, Inc.", "secteur": "Automobile"},
    "F": {"nom": "Ford Motor Company", "secteur": "Automobile"},
    "TM": {"nom": "Toyota Motor Corp.", "secteur": "Automobile"},
    "AMZN": {"nom": "Amazon.com, Inc.", "secteur": "Commerce électronique"},
    "BABA": {"nom": "Alibaba Group Holding", "secteur": "Commerce électronique"},
    "AAPL": {"nom": "Apple Inc.", "secteur": "Technologie"},
    "MSFT": {"nom": "Microsoft Corporation", "secteur": "Technologie"}
}

def collecter_et_sauvegarder():
    api = GestionnaireAPI()
    try:
        donnees_financieres, actualites = api.collecter_donnees_entreprises(NOMS_ENTREPRISES)
        GestionnaireFichier.sauvegarder_donnees_entreprises(donnees_financieres, dossier="data/financieres")
        GestionnaireFichier.sauvegarder_donnees_entreprises(actualites, dossier="data/actualites")
        logger.info("Données financières et actualités sauvegardées dans les fichiers CSV.")
    except Exception as e:
        logger.error(f"Erreur lors de la collecte ou de la sauvegarde des données : {e}")


if __name__ == "__main__":
    collecter_et_sauvegarder()
