import sys
import os

# Ajouter le dossier `src/` au chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from gestionnaire_fichier import GestionnaireFichier

@pytest.fixture
def sample_data():
    return [{"Date": "2024-11-26", "Open": "1000.0", "High": "1050.0", "Low": "950.0", "Close": "1005.0", "Volume": "5000000"}]

def test_sauvegarder_et_charger_csv(tmp_path, sample_data):
    fichier = tmp_path / "test.csv"
    GestionnaireFichier.sauvegarder_csv(str(fichier), sample_data, sample_data[0].keys())
    loaded_data = GestionnaireFichier.charger_donnees_csv(str(fichier))
    assert len(loaded_data) == len(sample_data)
    assert loaded_data[0]["Date"] == sample_data[0]["Date"]

def test_charger_csv_fichier_inexistant():
    with pytest.raises(Exception, match="Fichier introuvable"):
        GestionnaireFichier.charger_donnees_csv("non_existant.csv")
