# Projet FW1-CC1-Gr-15
## Membres du groupe
- Kamilia Hacini - [kamilia.hacini@etu.univ-orleans.fr](mailto:kamilia.hacini@etu.univ-orleans.fr)
- Sarah Chibane - [sarah.chibane@etu.univ-orleans.fr](mailto:sarah.chibane@etu.univ-orleans.fr)
- Elyes Fetmouche- [elyes.fetmouche@etu.univ-orleans.fr](mailto:elyes.fetmouche@etu.univ-orleans.fr)
- Rayane Touak- [rayane.touak@etu.univ-orleans.fr](mailto:rayane.touak@etu.univ-orleans.fr)

## Question 1: Mise en place du projet Django

## Commande utilisées

#Creation et lancement du conteneur et l'image docker
docker-compose buid
USERNAME=$(basename $(id -un) @campus.univ-orleans.fr) USERID=$(id -u) docker-compose up -d

#Creation du projet Django
django-admin startproject cc .

#Creation de l'application Django
python manage.py startapp medico 

#L ajout de l'application 'medico' dans cc/setting.py
#INSTALLED_APPS = [ 'medico' ]

#verification du serveur Django
python manage.py runserver 0.0.0.0:8000
## Question 2 :Vue et template "About"


## Commandes

-Etape 1:Création du template 'about.html' dans 'medico/templates/medico/'

-Etape2:Création de la vue 'about' dans 'medico/view.py'

-Etape3:Ajout du chemin medico/urls.py

-Etape4:Ajout de URLS de l'app dans le projet cc

-Etape5: verification serveur Django:python manage.py runserver 0.0.0.0:8000


## Question 3 : Création du modéle Consultation

## Objectif

Création d'un modèle 'Consultation' dans l'application 'medico'
 -'patient_nom' : chaine de caractères
-'patient_prenom' : chaine de caractères
-'patient_genre': choix entre Homme et Femme
'patient_age' :entier positif
-'description' = texte
-'date_consultation' = auto date

aucun de ces champs ne peut recevoir la valeur 'null'

## Choix justifier
-'patient_genre' utilise 'choices=[('M','Homme'),('F','Femme')] pour limiter les valeurs
-'date_consultation' date automatiques.

## etapes 

-Creation du modéle dans 'medico/modelspy'

## applicatioon de la migration
python manage.py makemigrations medico
python manage.py migrate
## Question 4 
fixtures JSON pour les consultations
-Etapes realisees:

1. creation des consultations : 
12 consultations generées par IA

2.  le fichier.json est situé dans medico/fixtures/.

-Chaque consultation contient des champs correspondant au modele.

- Pour charger les données dans la base :

   python manage.py loaddata examples

   puis vérifier  avec les commandes :

   - from medico.models import Consultation
   - Consultation.objects.count()
   - Consultation.objects.first()





## Question 2 :Vue et template "About"


## Commandes

-Etape 1:Création du template 'about.html' dans 'medico/templates/medico/'

-Etape2:Création de la vue 'about' dans 'medico/view.py'

-Etape3:Ajout du chemin medico/urls.py

-Etape4:Ajout de URLS de l'app dans le projet cc

-Etape5: verification serveur Django:python manage.py runserver 0.0.0.0:8000


## Question 3 : Création du modéle Consultation

## Objectif

Création d'un modèle 'Consultation' dans l'application 'medico'
 -'patient_nom' : chaine de caractères
-'patient_prenom' : chaine de caractères
-'patient_genre': choix entre Homme et Femme
'patient_age' :entier positif
-'description' = texte
-'date_consultation' = auto date

aucun de ces champs ne peut recevoir la valeur 'null'

## Choix justifier
-'patient_genre' utilise 'choices=[('M','Homme'),('F','Femme')] pour limiter les valeurs
-'date_consultation' date automatiques.

## etapes 

-Creation du modéle dans 'medico/modelspy'

## applicatioon de la migration
python manage.py makemigrations medico
python manage.py migrate



