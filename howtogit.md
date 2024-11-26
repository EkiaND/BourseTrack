# Guide pour Utiliser Git avec le Projet BourseTrack

Ce guide explique comment effectuer des modifications dans le dépôt, les committer et les pousser sur GitHub.

---

## 1. Cloner le Dépôt

Si ce n'est pas encore fait, commencez par cloner le dépôt sur votre machine locale :

```bash
git clone https://github.com/<votre-utilisateur>/BourseTrack.git
```
Déplacez-vous dans le répertoire cloné : 

```bash
cd BourseTrack
```

---

## 2. Faire des modifications

1. Modifiez ou ajoutez des fichiers dans le projet sur vsc comme d'habitude.
2. Vérifiez les modifiés ou ajoutés avec : 

```bash
git status
```
---

## 3. Ajouter les Fichiers Modifiés au Suivi

Une fois vos modification prêtes, ajoutez-les au suivi Git : 

- Ajouter un fichier spécifique

```bash
git add nom_du_fichier 
```
- Ajouter tous les fichiers modifiés d'un coup 

```bash
git add .
```

---

## 4. Créer un Commit

Un commit enregistre vos modification localement. Ajoutez un message décrivant vos changements : 

```bash
git commit -m "Description des modifications"
```

Exemples de messages clairs : 

- "Ajout de la classe GestionnaireAPI"
- "Correction du bug sur l'affichage des graphiques"
- "Mise à jour du README.md"

---

## 5. Pousser les Modifications vers GitHub

Envoyez vos commits locaux vers le dépôt GitHub distant avec la commande suivante :

```bash
git push
```

---

## 6. Récupérer les Derniers Changements (si d'autres personnes ont push depuis la dernière fois que vous avez récupérer le repo)

Si plusieurs personnes travaillent sur le projet, il est recommandé de récupérer les dernières modifications avant de push les vôtres : 

```bash
git pull
```
Ensuite, répétez les étapes de add, commit, et push.



