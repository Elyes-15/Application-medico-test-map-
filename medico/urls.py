
from django.urls import path
from . import views
urlpatterns= [
  
    path('about', views.about, name='about'),
    path('consultation/<int:n>/', views.details_consultation,name='details_consultation'),
    path('consultations/', views.consultation_list,name='liste_consultaiton'),
]

