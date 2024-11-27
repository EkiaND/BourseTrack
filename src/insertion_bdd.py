import os
from gestionnaire_logs import logger
from gestionnaire_bdd import GestionnaireBDD, Entreprise
from gestionnaire_fichier import GestionnaireFichier
from datetime import datetime

NOMS_ENTREPRISES = {
    "TSLA": {"nom": "Tesla, Inc.", "secteur": "Automobile"},
    "F": {"nom": "Ford Motor Company", "secteur": "Automobile"},
    "TM": {"nom": "Toyota Motor Corp.", "secteur": "Automobile"},
    "AMZN": {"nom": "Amazon.com, Inc.", "secteur": "Commerce électronique"},
    "BABA": {"nom": "Alibaba Group Holding", "secteur": "Commerce électronique"},
    "AAPL": {"nom": "Apple Inc.", "secteur": "Technologie"},
    "MSFT": {"nom": "Microsoft Corporation", "secteur": "Technologie"}
}

class InsertionBDD:
    def __init__(self):
        self.gestionnaire_bdd = GestionnaireBDD()  # Initialisation du gestionnaire de base de données

    def valider_donnees(self, donnees):
        """
        Valide les données avant l'insertion dans la base de données.
        :param donnees: Liste de dictionnaires contenant les données.
        :return: Liste des données valides.
        """
        donnees_valides = []
        for data in donnees:
            try:
                # Vérification des champs nécessaires
                assert "date" in data and isinstance(data["date"], datetime.date)
                assert "open" in data and isinstance(data["open"], (float, int))
                assert "high" in data and isinstance(data["high"], (float, int))
                assert "low" in data and isinstance(data["low"], (float, int))
                assert "close" in data and isinstance(data["close"], (float, int))
                assert "volume" in data and isinstance(data["volume"], int)
                # Ajouter aux données valides si tout est OK
                donnees_valides.append(data)
            except AssertionError as e:
                print(f"Données invalides ignorées : {data}")
        return donnees_valides
    
    def traiter_et_inserer(self, dossier="data/financieres"):
        fichiers_csv = self.get_fichiers_csv(dossier)
        for fichier in fichiers_csv:
            if os.path.getsize(fichier) == 0:
                raise Exception(f"Erreur de format : le fichier {fichier} est vide.")

            symbole = os.path.basename(fichier).split(".")[0]
            entreprise = NOMS_ENTREPRISES.get(symbole)

            if not entreprise:
                raise Exception(f"Erreur : le symbole {symbole} n'est pas reconnu.")

            secteur = entreprise["secteur"]

            # Ajoute l'entreprise si elle n'existe pas déjà
            if not self.gestionnaire_bdd.entreprise_existe(symbole):
                self.gestionnaire_bdd.ajouter_entreprise(symbole, entreprise["nom"], secteur)

            donnees = GestionnaireFichier.charger_donnees_csv(fichier)
            if not donnees:
                raise Exception(f"Erreur de format : le fichier {fichier} est vide.")

            donnees_traites = self.formater_donnees_pour_insertion(donnees, secteur)
            self.gestionnaire_bdd.ajouter_donnees_financieres(donnees_traites, symbole)

    def get_fichiers_csv(self, dossier):
        """
        Récupère tous les fichiers CSV dans un dossier donné.
        :param dossier: Le dossier contenant les fichiers CSV.
        :return: Liste des fichiers CSV.
        """
        fichiers = []
        for filename in os.listdir(dossier):
            if filename.endswith(".csv"):
                fichiers.append(os.path.join(dossier, filename))
        return fichiers

    def formater_donnees_pour_insertion(self, donnees, secteur):
        """
        Formate les données pour les rendre compatibles avec la base de données.
        :param donnees: Données chargées depuis le fichier CSV.
        :return: Données prêtes pour l'insertion.
        """
        donnees_formatees = []
        for ligne in donnees:
            try:
                donnees_formatees.append({
                    "date": datetime.strptime(ligne["Date"], "%Y-%m-%d").date(),
                    "open": float(ligne["Open"]),
                    "high": float(ligne["High"]),
                    "low": float(ligne["Low"]),
                    "close": float(ligne["Close"]),
                    "volume": int(ligne["Volume"]),
                    "secteur": secteur  # Ajout du secteur ici
                })
            except KeyError as e:
                print(f"Erreur de format pour la ligne {ligne}: {e}")
        return donnees_formatees

if __name__ == "__main__":
    insertion = InsertionBDD()
    insertion.traiter_et_inserer(dossier="data/financieres")
