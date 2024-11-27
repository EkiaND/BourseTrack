import sys
import os

# Ajouter le dossier `src/` au chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from gestionnaire_app import app
from gestionnaire_bdd import GestionnaireBDD, DonneeFinanciere

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_gestionnaire_bdd(mocker):
    """
    Fixture pour remplacer le comportement de la session de GestionnaireBDD
    dans les tests.
    """
    mock_session = mocker.Mock()
    mock_session.query.return_value.all.return_value = []  # Retourne une liste vide
    mocker.patch("gestionnaire_app.GestionnaireBDD.Session", return_value=mock_session)
    return mock_session

def test_index_page(client, mocker):
    # Création d'une instance de GestionnaireBDD mockée
    mock_gestionnaire_bdd = mocker.Mock()
    mock_session = mocker.Mock()
    mock_query = mocker.Mock()
    mock_query.all.return_value = []  # Simuler une base vide
    mock_session.query.return_value = mock_query
    mock_gestionnaire_bdd.Session.return_value = mock_session

    # Remplacement de l'instance GestionnaireBDD par une instance mockée
    mocker.patch("gestionnaire_app.GestionnaireBDD", return_value=mock_gestionnaire_bdd)

    # Appel de la route
    response = client.get("/")
    assert response.status_code == 200
    assert b"BourseTrack" in response.data



