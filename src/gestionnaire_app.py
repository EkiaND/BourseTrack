import os
import csv
import matplotlib
matplotlib.use('Agg')  # Backend sans interface graphique pour matplotlib
import matplotlib.pyplot as plt
from flask import Flask, render_template
from gestionnaire_bdd import GestionnaireBDD, DonneeFinanciere
from datetime import datetime
import locale


# Paramétrer la locale en français
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

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


def generer_html(indicateurs, graphique=None):
    # Filtrer les entreprises ayant une tendance >= 0
    entreprises_filtrees = [e for e in indicateurs if e["tendance_globale"] >= 0]

    # Lire les actualités pertinentes
    actualites = {}
    for entreprise in entreprises_filtrees:
        symbole = entreprise["symbole"]
        nom = entreprise["nom"]
        fichier_actualites = os.path.join(BASE_DIR, '../data/actualites', f'{symbole}.csv')
        if os.path.exists(fichier_actualites):
            with open(fichier_actualites, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                actualites[nom] = []
                count = 0
                for actualite in reader:
                    if count >= 3:
                        break
                    actualite["PublishedAt"] = datetime.strptime(actualite["PublishedAt"], "%Y-%m-%dT%H:%M:%SZ").strftime("%d %B %Y, %H:%M")
                    actualites[nom].append(actualite)
                    count += 1

    # Générer le HTML
    return render_template(
        'index.html',
        entreprises=entreprises_filtrees,
        actualites=actualites,
        indicateurs=indicateurs,
        graphique=graphique  # Ajouter le graphique au contexte
    )




def afficher_volume_total():
    """
    Génère deux versions (claire et sombre) du graphique circulaire pour le volume total des échanges.
    """
    volumes = bdd.volume_total_par_entreprise()

    if volumes:
        noms = [vol[0] for vol in volumes]
        valeurs = [vol[1] for vol in volumes]

        # Paramètres communs
        figure_params = {
            'figsize': (10, 10)  # Taille de la figure
        }
        
        pie_params = {
            'labels': noms,
            'autopct': '%1.1f%%',
            'startangle': 90,
            'pctdistance': 0.85,
            'labeldistance': 1.1,
            'textprops': {'fontsize': 9}
        }

        # Style pour le mode clair
        plt.style.use('default')
        plt.figure(**figure_params)
        wedges, texts, autotexts = plt.pie(valeurs, **pie_params)
        plt.title("Volume Total des Échanges par Entreprise")
        
        # Ajuster la disposition des labels
        plt.setp(autotexts, size=8)
        plt.setp(texts, size=8)
        
        graphique_filename_light = "images/volume_total_light.jpg"
        graphique_path_light = os.path.join(app.static_folder, graphique_filename_light)
        os.makedirs(os.path.dirname(graphique_path_light), exist_ok=True)
        plt.savefig(graphique_path_light, facecolor='#f4f4f4', bbox_inches='tight', dpi=300)
        plt.close()

        # Style pour le mode sombre
        plt.style.use('dark_background')
        plt.figure(**figure_params)
        wedges, texts, autotexts = plt.pie(valeurs, **pie_params)
        plt.title("Volume Total des Échanges par Entreprise")
        
        # Ajuster la disposition des labels
        plt.setp(autotexts, size=8)
        plt.setp(texts, size=8)
        
        graphique_filename_dark = "images/volume_total_dark.jpg"
        graphique_path_dark = os.path.join(app.static_folder, graphique_filename_dark)
        plt.savefig(graphique_path_dark, facecolor='#131313', bbox_inches='tight', dpi=300)  # Fond sombre modifié
        plt.close()

        return {
            'light': graphique_filename_light,
            'dark': graphique_filename_dark
        }
    return None


@app.route("/")
def index():
    """
    Route principale pour afficher les indicateurs financiers, le graphique et les actualités.
    """
    indicateurs = bdd.calculer_indicateurs_financiers()
    graphique_path = afficher_volume_total()  # Chemin relatif à static

    return generer_html(indicateurs, graphique=graphique_path)


if __name__ == "__main__":
    app.run(debug=True)