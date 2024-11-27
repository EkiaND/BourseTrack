import sys
import os

# Ajouter le dossier `src/` au chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from gestionnaire_fichier import GestionnaireFichier

def test_sauvegarder_csv():
    nom_fichier = "test_donnees.csv"
    donnees = [
        {"Date": "2024-11-26", "Open": 341.00, "High": 346.96, "Low": 335.66, "Close": 338.23, "Volume": 61307889},
        {"Date": "2024-11-25", "Open": 360.14, "High": 361.93, "Low": 338.20, "Close": 338.59, "Volume": 95890899}
    ]
    entetes = ["Date", "Open", "High", "Low", "Close", "Volume"]
    
    try:
        GestionnaireFichier.sauvegarder_csv(nom_fichier, donnees, entetes)
        assert os.path.exists(nom_fichier), "Le fichier CSV n'a pas été créé."
        print("Test `sauvegarder_csv` réussi.")
    except Exception as e:
        print(f"Erreur dans `sauvegarder_csv`: {e}")
    finally:
        if os.path.exists(nom_fichier):
            os.remove(nom_fichier)

if __name__ == "__main__":
    test_sauvegarder_csv()
