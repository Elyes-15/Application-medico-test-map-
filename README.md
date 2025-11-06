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



## Commandes

-Etape 1:Création du template 'about.html' dans 'medico/templates/medico/'

-Etape2:Création de la vue 'about' dans 'medico/view.py'

-Etape3:Ajout du chemin medico/urls.py

-Etape4:Ajout de URLS de l'app dans le projet cc

-Etape5: verification serveur Django:python manage.py runserver 0.0.0.0:8000


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



### Question 5: Afficher les détails d'une ocnsultation
**Objectif**: Créer une vue et le template associé pour afficher les détails d’une consultation.
 L’URL d’accès doit être /consultations/n où n est l'dentifiant de la consultation

 **Commandes et étapes suivis**:

 **Création de la vue détails** dans 'medico/views.py' de la manière suivante:
 def details_consultation(request, n):
    consultation = Consultation.objects.get(id = n)
    return render(request, 'medico/details_consultation.html', {'consultation': consultation})

**Ajout de l'url** dans 'medico/urls.py' de la manière suivante:
path('consultation/<int:n>/', views.details_consultation, name = 'details_consultation'),

**Création de la template**: nommée 'detail_consultation.html' dans lequel nous avons:
- Afficher toutes les informations concernant le patient et de la consultation
- ajouter un lien de retour vers la liste des consultations initiale

### Question 6 : Liste des consultations

**Objectif** : Créer une vue et un template pour afficher la liste des consultations sous forme tabulaire à l'URL `/consultations`.

**Commandes et étapes** :

**Création de la vue liste** dans `medico/views.py` de la manière suivante:
def consultation_list(request):
consultations = Consultation.objects.all()
 return render(request, 'medico/liste_consultation.html', {'consultation': consultation}),
**Ajout de l'url** dans 'medico/urls.py' de la manière suivante:
path('consultations/', views.consultation_list, 'liste_consultaiton'),
**Création de la template**: nommée 'liste_consultation.html' dans lequel nous avons:
- Afficher la liste des consultations sous forme de tableau avec toutes les informations du patient
- Description tronquée à 20 caractères avec le filtre truncatechars:20
- Lien vers la fiche détaillée de chaque consultation

### Question7
-Ajout de nouvelle_consultation

-Ajout de sa vue

-Ajout de son urls

### Question 8 : Suppression d’une consultation
**Objectif** : Créer une vue et un template permettant de supprimer une consultation existante avec confirmation avant suppression.

**ETAPES**


1-Création de la vue effacer_consultation dans medico/views.py : 
    
     -récupération de la consultation via get_object_or_404.

     - suppression de la consultation et redirection vers la liste.
    
    -affichage d’une page de confirmation.(si post)


2-Ajout de l’URL correspondante dans medico/urls.py: path('effacer_consultation/<int:consultation_id>/', views.effacer_consultation, name='effacer_consultation')


3-Création du template effacer_consultation.html dans medico/templates/medico/:
    
     -Affiche les informations de la consultation.
     -Bouton pour confirmer la suppression.
     -Lien pour annuler et revenir à la liste.

4-Modification du template liste_consultation.html :
    
    -Ajout d’un lien “Supprimer” pour chaque consultation.
     


# Question 9 – Modification d’une consultation

1. Création d’une **vue `changer_consultation`** dans `medico/views.py` :
   - Récupère la consultation à modifier via son `id`.
   - Si la requête est POST, met à jour les champs modifiables et sauvegarde.
   - Sinon, affiche le formulaire avec les informations existantes.

2. Création d’un **template `changer_consultation.html`** dans `medico/templates/medico/` :
   - Formulaire qui affiche les champs modifiable de la consultation.
   - Bouton “Enregistrer” pour soumettre les modifications.
   - Lien “Retour à la liste” vers la page des consultations.

3. Mise à jour de `medico/urls.py` :
```python
path('changer_consultation/<int:n>/', views.changer_consultation, name='changer_consultation'),
 ## Question 10:Création d’un template principal et d’un menu commun
1.Création du template principal (base.html)
- Contient la structure HTML générale du site.
 - Inclut un en-tête et un menu de navigation commun.
   

2. Héritage dans les autres templates
- Chaque page spécifique hérite du template principal.


3.Définition de l’URL racine
- Configurer l’URL `/` pour qu’elle affiche la page principale.


4. Amélioration esthétique avec Bootstrap
- Intégrer la bibliothèque **Bootstrap** dans le template principal.
 
 

 