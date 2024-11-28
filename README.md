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
│   .env
│   .gitignore
│   bourse.db
│   bourse_track.log
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
│   │
│   └───__pycache__
│           gestionnaire_api.cpython-311.pyc
│           gestionnaire_api.cpython-313.pyc
│           gestionnaire_app.cpython-313.pyc
│           gestionnaire_bdd.cpython-311.pyc
│           gestionnaire_bdd.cpython-312.pyc
│           gestionnaire_bdd.cpython-313.pyc
│           gestionnaire_fichier.cpython-313.pyc
│           gestionnaire_logs.cpython-313.pyc
│           insertion_bdd.cpython-313.pyc
│
├───static
│   ├───css
│   │       style.css
│   │
│   ├───images
│   │       volume_total.jpg
│   │
│   └───js
│           sorting.js
│           toggle-dark-mode.js
│
├───templates
│       index.html
│
└───test
    │   test_gestionnaire_api.py
    │   test_gestionnaire_app.py
    │   test_gestionnaire_bdd.py
    │   test_gestionnaire_fichier.py
    │   test_insertion_bdd.py
    │   __init__.py
    │
    └───__pycache__
            test_gestionnaire_api.cpython-313-pytest-8.3.3.pyc
            test_gestionnaire_app.cpython-313-pytest-8.3.3.pyc
            test_gestionnaire_bdd.cpython-313-pytest-8.3.3.pyc
            test_gestionnaire_fichier.cpython-313-pytest-8.3.3.pyc
            test_insertion_bdd.cpython-313-pytest-8.3.3.pyc
            __init__.cpython-313.pyc
```

---

# Auteurs

## Lesueur Romain

-
-
-

## Sidy Diop

-
-
-

## Saint-Hubert Courteney

-
-
-


---
Ce **README.md** est structuré pour fournir toutes les informations essentielles aux utilisateurs et développeurs. Si des ajustements ou des sections supplémentaires sont nécessaires, dites-le-moi !
