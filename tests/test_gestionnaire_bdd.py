import sys
import os
import sqlalchemy
import pytest
import gc
from datetime import date
from typing import Any

# Ajouter le dossier `src/` au chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
print(sys.path)  # Debugging line to ensure the path is correct
"['\\\\calebasse\\lesueur221\\Bureau\\2024-2025\\BT\\BourseTrack\\src', '\\\\calebasse\\lesueur221\\Bureau\\2024-2025\\BT\\BourseTrack\\tests', 'C:\\Users\\lesueur221\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip', 'C:\\Users\\lesueur221\\AppData\\Local\\Programs\\Python\\Python313\\DLLs', 'C:\\Users\\lesueur221\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 'C:\\Users\\lesueur221\\AppData\\Local\\Programs\\Python\\Python313', 'C:\\Users\\lesueur221\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']"

from gestionnaire_bdd import GestionnaireBDD, Entreprise, DonneeFinanciere

@pytest.fixture
def bdd():
    db_path = "test_bourse.db"
    if os.path.exists(db_path):
        # Fermer toutes les connexions existantes
        engine = sqlalchemy.create_engine(f"sqlite:///{db_path}")
        engine.dispose()
        gc.collect()  # Libérer les objets SQLAlchemy en mémoire
        try:
            os.remove(db_path)
        except Exception as e:
            print(f"Erreur lors de la suppression de {db_path}: {e}")

    gestionnaire = GestionnaireBDD(nom_bdd=db_path)
    yield gestionnaire

    # Nettoyer après les tests
    if os.path.exists(db_path):
        engine.dispose()
        gc.collect()
        try:
            os.remove(db_path)
        except Exception as e:
            print(f"Erreur lors du nettoyage de {db_path}: {e}")

def test_ajouter_et_recuperer_entreprise(bdd: Any):
    bdd.ajouter_entreprise("TSLA", "Tesla, Inc.", "Automobile")
    session = bdd.Session()
    entreprise = session.query(Entreprise).filter_by(symbole="TSLA").first()
    session.close()
    assert entreprise is not None
    assert entreprise.nom == "Tesla, Inc."
    assert entreprise.secteur == "Automobile"


def test_ajouter_donnees_financieres(bdd: Any):
    bdd.ajouter_entreprise("TSLA", "Tesla, Inc.", "Automobile")
    donnees = [
        {"date": date(2024, 11, 26), "open": 1000.0, "high": 1050.0, "low": 950.0, "close": 1005.0, "volume": 5000000}
    ]
    bdd.ajouter_donnees_financieres(donnees, "TSLA")
    session = bdd.Session()
    donnees_financieres = session.query(DonneeFinanciere).filter_by(symbole="TSLA").all()
    session.close()
    assert len(donnees_financieres) == 1
    assert donnees_financieres[0].secteur == "Automobile"  # Validation du secteur


def test_ajout_entreprise_duplicat(bdd: Any):
    bdd.ajouter_entreprise("TSLA", "Tesla, Inc.", "Automobile")
    with pytest.raises(Exception, match="Entreprise avec le symbole TSLA existe déjà."):
        bdd.ajouter_entreprise("TSLA", "Tesla, Inc.", "Automobile")
