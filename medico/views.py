from django.shortcuts import render, redirect, get_object_or_404
from .models import Consultation

def about(request):
    return render(request, 'medico/about.html')

def details_consultation(request, n):
    consultation = Consultation.objects.get(id = n)
    return render(request, 'medico/details_consultation.html', {'consultation': consultation})

def consultation_list(request):
    consultations = Consultation.objects.all()
    return render(request, 'medico/liste_consultation.html', {'consultations': consultations})

