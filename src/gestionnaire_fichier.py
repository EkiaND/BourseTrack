import csv
import os

class GestionnaireFichier:
    
    @staticmethod
    def sauvegarder_csv(nom_fichier, donnees, entetes):
        """
        Sauvegarde des données dans un fichier CSV.
        :param nom_fichier: Chemin du fichier
        :param donnees: Liste des données
        :param entetes: Liste des colonnes
        """
        with open(nom_fichier, mode="w", newline="", encoding="utf-8") as fichier:
            writer = csv.DictWriter(fichier, fieldnames=entetes)
            writer.writeheader()
            writer.writerows(donnees)
            
    @staticmethod
    def sauvegarder_donnees_entreprises(donnees, dossier="data"):
        """
        Sauvegarde les données financières et les actualités de plusieurs entreprises.
        :param donnees: Dictionnaire contenant les données à sauvegarder.
        :param dossier: Dossier où sauvegarder les fichiers.
        """
        os.makedirs(dossier, exist_ok=True)
        for symbole, data in donnees.items():
            nom_fichier = os.path.join(dossier, f"{symbole}.csv")
            entetes = data[0].keys() if data else []
            GestionnaireFichier.sauvegarder_csv(nom_fichier, data, entetes)
            
    @staticmethod
    def charger_donnees_csv(chemin_fichier):
        """
        Charge les données d'un fichier CSV dans une liste de dictionnaires.
        :param chemin_fichier: Chemin du fichier CSV à lire.
        :return: Liste de dictionnaires contenant les données.
        """
        try:
            with open(chemin_fichier, mode='r', encoding='utf-8') as fichier:
                lecteur = csv.DictReader(fichier)
                return [ligne for ligne in lecteur]
        except FileNotFoundError:
            raise Exception(f"Fichier introuvable : {chemin_fichier}")
        except Exception as e:
            raise Exception(f"Erreur lors du chargement du fichier CSV : {e}")
            
            
