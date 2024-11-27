import sys
import os

# Ajouter le dossier `src/` au chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from gestionnaire_app import app

def test_index_route():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200, "La route '/' doit renvoyer un code 200."
    assert b"BourseTrack" in response.data, "La page doit contenir le mot 'BourseTrack'."
    print("Test `index_route` réussi.")

if __name__ == "__main__":
    test_index_route()
