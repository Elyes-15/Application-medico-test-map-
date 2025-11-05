<<<<<<< HEAD
from django.shortcuts import render
<<<<<<< HEAD
def about(request):
    return render(request, 'medico/about.html')
# Create your views here.
=======
=======
from django.shortcuts import render, redirect, get_object_or_404
>>>>>>> 2bf63f234f1c9ec37db349ba8a1656e3a115f662
from .models import Consultation

def about(request):
    return render(request, 'medico/about.html')

def details_consultation(request, n):
    consultation = Consultation.objects.get(id = n)
    return render(request, 'medico/details_consultation.html', {'consultation': consultation})

def consultation_list(request):
    consultations = Consultation.objects.all()
    return render(request, 'medico/liste_consultation.html', {'consultations': consultations})

