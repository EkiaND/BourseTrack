import os
from flask import Flask, render_template
from gestionnaire_api import GestionnaireAPI
from gestionnaire_fichier import GestionnaireFichier
from gestionnaire_bdd import GestionnaireBDD

# Création de l'application Flask en précisant le dossier des templates
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "../templates"))

@app.route("/")
def index():
    return render_template("index.html", titre="BourseTrack")

if __name__ == "__main__":
    app.run(debug=True)