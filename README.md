# BourseTrack

**BourseTrack** est une application web conçue pour suivre et analyser les performances financières des grandes entreprises, enrichies par des actualités pertinentes pour offrir une compréhension globale des tendances économiques.

---

## Fonctionnalités

- **Suivi des performances financières** :
  - Prix moyen d'ouverture et de clôture.
  - Volatilité moyenne et rendements journaliers.
  - Volumes d'échanges et tendances globales.
- **Analyse contextuelle** :
  - Actualités pertinentes associées aux entreprises suivies.
  - Présentation des données sous forme de tableaux et graphiques.
- **Interface intuitive** :
  - Page web dynamique générée via Flask.

---

## Technologies

- **Langage principal** : Python 3.12.X
- **Framework web** : Flask
- **Base de données** : SQLite
- **Visualisation** : matplotlib, seaborn
- **APIs utilisées** :
  - [Alpha Vantage](https://www.alphavantage.co/) : Données financières.
  - [News API](https://newsapi.org/) : Actualités du marché.

---

## Installation

### Prérequis

- Python 3.x doit être installé sur votre machine.
- Les clés d'API pour [Alpha Vantage](https://www.alphavantage.co/) et [News API](https://newsapi.org/) sont nécessaires.

### Étapes d'installation

1. Clonez le dépôt :

```bash
   git clone https://github.com/EkiaND/BourseTrack.git
   cd BourseTrack
```

2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

3. Configurez les clés d'API

- Créez un fichier .env à la racine du projet avec le contenu suivant :

```makefile
ALPHA_VANTAGE_KEY= A REMPLACER PAR VOTRE CLE API
NEWS_API_KEY= A REMPLACER PAR VOTRE CLE API
```

4. Lancez l'application :

```bash
python src/gestionnaire_app.py
```


---

# Structure du projet 

```bash
BourseTrack
│   .gitignore
│   bourse.db
│   howtogit.md
│   README.md
│   requirements.txt
│
├───data
│   ├───actualites
│   │       AAPL.csv
│   │       AMZN.csv
│   │       BABA.csv
│   │       F.csv
│   │       MSFT.csv
│   │       TM.csv
│   │       TSLA.csv
│   │
│   └───financieres
│           AAPL.csv
│           AMZN.csv
│           BABA.csv
│           F.csv
│           MSFT.csv
│           TM.csv
│           TSLA.csv
│
├───src
│   │   collecte_donnees.py
│   │   gestionnaire_api.py
│   │   gestionnaire_app.py
│   │   gestionnaire_bdd.py
│   │   gestionnaire_fichier.py
│   │   gestionnaire_logs.py
│   │   insertion_bdd.py
│   │   __init__.py
│
├───static
│   ├───css
│   │       style.css
│   │
│   ├───images
│   │       volume_total_dark.jpg
│   │       volume_total_light.jpg
│   └───js
│           sorting.js
│           toggle-dark-mode.js
│
├───templates
│       index.html


```

---

# Auteurs

## Lesueur Romain

Partie Collecte des Données (APIs et CSV)

- Développement complet des scripts pour collecter les données financières via les APIs suivantes :
  - [Alpha Vantage](https://www.alphavantage.co/) : Données financières.
  - [News API](https://newsapi.org/) : Actualités du marché.

- Mise en place de la logique de stockage des données en fichiers CSV.
- Gestion des formats et organisation des fichiers pour garantir une compatibilité avec les autres parties du projet.

## Sidy Diop

Base de Données (SQLite avec SQLAlchemy)

- Conception et mise en place de la base de données SQLite pour le stockage structuré des données.
- Intégration de SQLAlchemy pour faciliter les interactions entre les scripts et la base de données.
- Écriture des requêtes permettant d’extraire les indicateurs financiers utilisés dans l’application web.

## Saint-Hubert Courteney

Application Web (Flask et Jinja2)

- Développement complet du site web basé sur Flask, y compris la gestion des routes et des templates.
- Création des interfaces utilisateur en utilisant Jinja2 pour afficher les données financières et les graphiques.
- Intégration des visualisations générées par Matplotlib et gestion des actualités associées aux entreprises.
