from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('consultation/<int:n>/', views.details_consultation, name='details_consultation'),
    path('consultations/', views.consultation_list, name='liste_consultation'),
    path('consultations/effacer/<int:consultation_id>/', views.effacer_consultation, name='effacer_consultation'),
    path('changer_consultation/<int:consultation_id>/', views.changer_consultation, name='changer_consultation'),
    path('nouvelle_consultation/', views.ajouter_consultation, name='ajouter_consultation'),


]
