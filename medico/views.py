from django.shortcuts import render
from .models import Consultation

def about(request):
    return render(request, 'medico/about.html')

def details_consultation(request, n):
    consultation = Consultation.objects.get(id = n)
    return render(request, 'medico/details_consultation.html', {'consultation': consultation})