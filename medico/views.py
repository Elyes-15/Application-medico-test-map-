from django.shortcuts import render
<<<<<<< HEAD
def about(request):
    return render(request, 'medico/about.html')
# Create your views here.
=======
from .models import Consultation

def about(request):
    return render(request, 'medico/about.html')

def details_consultation(request, n):
    consultation = Consultation.objects.get(id = n)
    return render(request, 'medico/details_consultation.html', {'consultation': consultation})

def consultation_list(request):
    consultations = Consultation.objects.all()
    return render(request, 'medico/liste_consultation.html', {'consultations': consultations})

>>>>>>> d8374caa018b1b9bc0817647b170cf460b9b82c5
