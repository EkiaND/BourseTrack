import sys
import os
import matplotlib.pyplot as plt

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

def generer_html():
    # Récupérer les données financières
    gestionnaire_bdd = GestionnaireBDD()
    entreprises = gestionnaire_bdd.Session.query(DonneeFinanciere).all()

    # Filtrer les entreprises ayant une tendance de 0.15 ou -0.15
    entreprises_filtrees = [e for e in entreprises if abs(e.tendance) >= 0.15]

    # Générer le graphique circulaire des volumes d'échange
    volumes = [e.volume for e in entreprises_filtrees]
    labels = [e.nom for e in entreprises_filtrees]
    plt.pie(volumes, labels=labels, autopct='%1.1f%%')
    plt.title('Volumes d\'échange')
    plt.savefig('static/volumes_echange.png')
    plt.close()

    # Lire les actualités pertinentes
    actualites = {}
    for entreprise in entreprises_filtrees:
        symbole = entreprise.symbole
        fichier_actualites = os.path.join('./data/actualites/', f'{symbole}.csv')
        if os.path.exists(fichier_actualites):
            with open(fichier_actualites, 'r') as f:
                actualites[symbole] = f.readlines()

    # Générer le HTML
    html = '<html><head><title>Actualités Financières</title></head><body>'
    html += '<h1>Actualités Financières</h1>'
    html += '<img src="static/volumes_echange.png" alt="Volumes d\'échange">'
    html += '<table border="1"><tr><th>Entreprise</th><th>Indicateurs Financiers</th><th>Actualités</th></tr>'
    for entreprise in entreprises_filtrees:
        symbole = entreprise.symbole
        html += f'<tr><td>{entreprise.nom}</td>'
        html += f'<td>Tendance: {entreprise.tendance}, Volume: {entreprise.volume}</td>'
        html += '<td>'
        if symbole in actualites:
            for actualite in actualites[symbole]:
                html += f'<p>{actualite}</p>'
        html += '</td></tr>'
    html += '</table></body></html>'

    return html

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



