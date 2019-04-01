# ISN_Projet_Final
Répertoire avec le projet d'ISN de fin d'année

plein de mini-jeux
-> morpion, snake, puissance 4, pac man, tetris, robot tete chercheuse, qui-est-ce?, space invaders,
pendu, pong, demineur

## mardi 26 mars 2019:  
début du projet et assemblage des idées

début de la tete chercheuse

Mise en place du repository GitHub avec syncronisation entre les ordinateurs.

## mercredi 27 mars 2019:
début réseau: Script pour transmetre un dictionnaire par TCP connection possible par pusieurs clients et la connection/déconnection est gérée

Finalisation du jeu de tête chercheuse

début de la création de l'interface principale

## Jeudi 28 mars 2019:
Bug de duplication du robot après 2ème essai
Bug : Inversement du sens du robot après 2ème essai
Bug sur le timer

Ajout de textures pour le jeux tête chercheuse et ajout pièces pour avoir un bonus de point

hébergement du serveur sur raspberry: le serveur est acessible en permanence


## Vendredi 29 mars 2019:
ajout de l'interface avec les règles du jeux et gestion de la fin ajout de la page du scoreboard au début du jeu

envoi du scoreboard avec les 10 meilleurs joueurs et stockage des données dans un fichier

Amélioration de la page des rêgles

## Samedi 30 mars 2019:
création de la classe scoreboard

création d'une fonction pour avoir les 10 meilleurs joueurs dans un jeu spécifique

## Dimanche 31 mars 2019:
création du classement Total dans la page principale

Bug: Départ à (-10)
Bug: non réactulisation de la variable (score) lors du restart, c'est a dire que la variable garde l'ancienne valeur et lui ajoute la nouvelle. Il devrait juste sauvegarder la nouvelle.

Ajout de la demande du pseudo au départ

serveur: ajout d'une fonction pour récupérer le score d'un joueur en particulier
