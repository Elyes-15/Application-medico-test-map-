
from django.urls import path
from . import views
urlpatterns= [
  
    path('about', views.about, name='about'),
<<<<<<< HEAD
=======
    path('consultation/<int:n>/', views.details_consultation,name='details_consultation'),
    path('consultations/', views.consultation_list,name='liste_consultaiton'),
>>>>>>> d8374caa018b1b9bc0817647b170cf460b9b82c5
]

