from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('consultation/<int:n>/', views.details_consultation, name='details_consultation'),
    path('consultations/', views.consultation_list, name='liste_consultation'),
    path('consultations/effacer/<int:consultation_id>/', views.effacer_consultation, name='effacer_consultation'),
    path('changer_consultation/<int:consultation_id>/', views.changer_consultation, name='changer_consultation'),
    path('nouvelle_consultation/', views.ajouter_consultation, name='ajouter_consultation'),
    path('ajouter_traitement/', views.ajouter_traitement, name='ajouter_traitement'),
    path('consultation/<int:consultation_id>/traitements/', views.consulter_traitements, name='consulter_traitements'),
    path('traitement/<int:pk>/edit/', views.traitement_edit, name='traitement_edit'),
    path('traitement/<int:pk>/delete/', views.traitement_delete, name='traitement_delete'),
    path('urgences/', views.liste_urgences, name='liste_urgences'),
    path('consultation/<int:consultation_id>/urgence/signaler/', views.signaler_urgence, name='signaler_urgence'),
    path('urgence/<int:urgence_id>/traitee/', views.marquer_traitee, name='marquer_traitee'),
    path('urgence/<int:urgence_id>/supprimer/', views.supprimer_urgence, name='supprimer_urgence'),
]
