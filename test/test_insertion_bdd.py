import sys
import os
import pytest
from datetime import date

# Ajouter le dossier `src/` au chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from insertion_bdd import InsertionBDD
from gestionnaire_fichier import GestionnaireFichier
from gestionnaire_bdd import DonneeFinanciere, Entreprise

@pytest.fixture
def sample_csv_data(tmp_path):
    data = [
        {"Date": "2024-11-26", "Open": "1000.0", "High": "1050.0", "Low": "950.0", "Close": "1005.0", "Volume": "5000000"}
    ]
    fichier = tmp_path / "TSLA.csv"
    GestionnaireFichier.sauvegarder_csv(str(fichier), data, data[0].keys())
    return str(fichier)

def test_insertion_bdd(sample_csv_data):
    inserter = InsertionBDD()

    session = inserter.gestionnaire_bdd.Session()
    session.query(DonneeFinanciere).delete()
    session.commit()
    session.close()

    inserter.gestionnaire_bdd.ajouter_entreprise("TSLA", "Tesla, Inc.", "Automobile")
    inserter.traiter_et_inserer(dossier=os.path.dirname(sample_csv_data))

    session = inserter.gestionnaire_bdd.Session()
    donnees_financieres = session.query(DonneeFinanciere).filter_by(symbole="TSLA").all()
    session.close()

    assert len(donnees_financieres) == 1
    assert donnees_financieres[0].secteur == "Automobile"
    assert donnees_financieres[0].close == 1005.0



def test_insertion_csv_vide(tmp_path):
    fichier_vide = tmp_path / "vide.csv"
    fichier_vide.touch()  # Crée un fichier vide
    inserter = InsertionBDD()
    with pytest.raises(Exception, match="Erreur de format : le fichier .* est vide"):
        inserter.traiter_et_inserer(dossier=tmp_path)


def test_insertion_entreprise_et_donnees(sample_csv_data):
    inserter = InsertionBDD()

    session = inserter.gestionnaire_bdd.Session()
    session.query(DonneeFinanciere).delete()
    session.query(Entreprise).delete()
    session.commit()
    session.close()

    inserter.traiter_et_inserer(dossier=os.path.dirname(sample_csv_data))

    # Vérifiez que l'entreprise a été créée
    session = inserter.gestionnaire_bdd.Session()
    entreprise = session.query(Entreprise).filter_by(symbole="TSLA").first()
    donnees_financieres = session.query(DonneeFinanciere).filter_by(symbole="TSLA").all()
    session.close()

    assert entreprise is not None
    assert entreprise.nom == "Tesla, Inc."
    assert entreprise.secteur == "Automobile"
    assert len(donnees_financieres) == 1
    assert donnees_financieres[0].close == 1005.0
