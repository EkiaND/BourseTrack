import csv

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
