import sys
import os

# Ajouter le dossier `src/` au chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from gestionnaire_bdd import GestionnaireBDD, DonneeFinanciere

def test_ajouter_donnees_financieres():
    gestionnaire_bdd = GestionnaireBDD("test_bourse.db")
    donnees = [
        {"date": "2024-11-26", "open": 341.00, "high": 346.96, "low": 335.66, "close": 338.23, "volume": 61307889},
        {"date": "2024-11-25", "open": 360.14, "high": 361.93, "low": 338.20, "close": 338.59, "volume": 95890899}
    ]
    
    try:
        gestionnaire_bdd.ajouter_donnees_financieres(donnees)
        session = gestionnaire_bdd.Session()
        resultats = session.query(DonneeFinanciere).all()
        assert len(resultats) == len(donnees), "Le nombre d'entrées dans la base doit correspondre."
        print("Test `ajouter_donnees_financieres` réussi.")
    except Exception as e:
        print(f"Erreur dans `ajouter_donnees_financieres`: {e}")
    finally:
        gestionnaire_bdd.engine.dispose()

if __name__ == "__main__":
    test_ajouter_donnees_financieres()
