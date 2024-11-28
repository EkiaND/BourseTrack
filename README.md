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
COURTENEY LA PLUS BELLE
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
