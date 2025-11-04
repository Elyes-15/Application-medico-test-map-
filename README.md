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

##Question 2 :Vue et template "About"


###Commandes

-Etape 1:Création du template 'about.html' dans 'medico/templates/medico/'

-Etape2:Création de la vue 'about' dans 'medico/view.py'

-Etape3:Ajout du chemin medico/urls.py

-Etape4:Ajout de URLS de l'app dans le projet cc

-Etape5: verification serveur Django:python manage.py runserver 0.0.0.0:8000





