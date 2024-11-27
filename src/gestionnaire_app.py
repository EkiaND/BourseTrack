import os
import matplotlib
matplotlib.use('Agg')  # Backend sans interface graphique pour matplotlib
import matplotlib.pyplot as plt
from flask import Flask, render_template
from gestionnaire_bdd import GestionnaireBDD

# Configuration de l'application Flask
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Dossier où se trouve gestionnaire_app.py
TEMPLATES_DIR = os.path.join(BASE_DIR, "../templates")
STATIC_DIR = os.path.join(BASE_DIR, "../static")

app = Flask(
    __name__,
    template_folder=TEMPLATES_DIR,  # Chemin absolu vers le dossier templates
    static_folder=STATIC_DIR        # Chemin absolu vers le dossier static
)
bdd = GestionnaireBDD()


def afficher_volume_total():
    """
    Génère un graphique circulaire pour le volume total des échanges par entreprise.
    """
    volumes = bdd.volume_total_par_entreprise()

    if volumes:
        noms = [vol[0] for vol in volumes]
        valeurs = [vol[1] for vol in volumes]

        # Génération du graphique
        plt.figure(figsize=(8, 8))
        plt.pie(valeurs, labels=noms, autopct='%1.1f%%', startangle=140)
        plt.title("Volume Total des Échanges par Entreprise")

        # Enregistrement du fichier dans le dossier static/images
        graphique_filename = "images/volume_total.jpg"
        graphique_path = os.path.join(app.static_folder, graphique_filename)
        os.makedirs(os.path.dirname(graphique_path), exist_ok=True)  # Crée le dossier si nécessaire
        plt.savefig(graphique_path)
        plt.close()

        # Retourne le chemin relatif pour Flask
        return graphique_filename
    return None


@app.route("/")
def index():
    """
    Route principale pour afficher les indicateurs financiers et le graphique.
    """
    indicateurs = bdd.calculer_indicateurs_financiers()
    graphique_path = afficher_volume_total()  # Chemin relatif à static

    return render_template(
        "index.html",
        titre="Performances Boursières",
        indicateurs=indicateurs,
        graphique=graphique_path  # Passe le chemin relatif au template
    )



if __name__ == "__main__":
    app.run(debug=True)
