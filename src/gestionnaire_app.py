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

        # Génération du graphique avec matplotlib
        plt.figure(figsize=(8, 8))
        plt.pie(valeurs, labels=noms, autopct='%1.1f%%', startangle=140)
        plt.title("Volume Total des Échanges par Entreprise")

        # Enregistrer le graphique dans le dossier static/images
        graphique_path = os.path.join(STATIC_DIR, "images", "volume_total.jpg")
        os.makedirs(os.path.dirname(graphique_path), exist_ok=True)  # Créer le dossier s'il n'existe pas
        plt.savefig(graphique_path)
        plt.close()
        return graphique_path
    return None


@app.route("/")
def index():
    """
    Route principale pour afficher les indicateurs financiers et le graphique.
    """
    indicateurs = bdd.calculer_indicateurs_financiers()
    graphique_path = afficher_volume_total()

    return render_template(
        "index.html",
        titre="Performances Boursières",
        indicateurs=indicateurs,
        graphique=graphique_path
    )


if __name__ == "__main__":
    app.run(debug=True)
