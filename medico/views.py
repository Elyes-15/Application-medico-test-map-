from django.shortcuts import render, redirect, get_object_or_404
from .models import Consultation
from .forms import ConsultationForm
from .models import Traitement
from .forms import TraitementForm
from .models import Urgence
from .forms import UrgenceForm
from .utils import geocode_address


def about(request):
    consultations = Consultation.objects.all()
    return render(request, 'medico/about.html', {'consultations': consultations})

def details_consultation(request, n):
    consultation = Consultation.objects.get(id = n)
    return render(request, 'medico/details_consultation.html', {'consultation': consultation})

def consultation_list(request):
    consultations = Consultation.objects.all()
    return render(request, 'medico/liste_consultation.html', {'consultations': consultations})
def ajouter_consultation(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)

            if consultation.patient_adresse:
                try:
                    lat, lon = geocode_address(consultation.patient_adresse)
                    consultation.latitude = lat
                    consultation.longitude = lon
                except Exception:
                    consultation.latitude = None
                    consultation.longitude = None

            consultation.save()
            return redirect('liste_consultation')  
    else:
        form = ConsultationForm()
    
    return render(request, 'medico/nouvelle_consultation.html', {'form': form})
def effacer_consultation(request, consultation_id):
    consultation = get_object_or_404(Consultation, pk=consultation_id)

    if request.method == 'POST':
        consultation.delete()
        return redirect('liste_consultation')
    return render(request, 'medico/effacer_consultation.html', {'consultation': consultation})

def changer_consultation(request, consultation_id):
    consultation = get_object_or_404(Consultation, id=consultation_id)

    if request.method == 'POST':
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            return redirect('liste_consultation')
    else:
        form = ConsultationForm(instance=consultation)

    return render(request, 'medico/changer_consultation.html', {'form': form, 'consultation': consultation})



def home(request):
    urgences_non_traitees = Urgence.objects.filter(traitee=False).count()
    return render(request, 'medico/home.html', {
        'urgences_non_traitees': urgences_non_traitees
    })




def ajouter_traitement(request):
    if request.method == "POST":
        form = TraitementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_consultation')  
    else:
        form = TraitementForm()
    return render(request, 'medico/ajouter_traitement.html', {'form': form})

def consulter_traitements(request, consultation_id):
    consultation = get_object_or_404(Consultation, id=consultation_id)
    traitements = Traitement.objects.filter(consultation=consultation)
    
    return render(request, 'medico/consulter_traitements.html', {
        'consultation': consultation,
        'traitements': traitements
    })
    
def traitement_delete(request, pk):
    traitement = get_object_or_404(Traitement, pk=pk)
    if request.method == "POST":
        traitement.delete()
        return redirect('consulter_traitements', consultation_id=traitement.consultation.id)
    return render(request, 'medico/traitement_confirm_delete.html', {'traitement': traitement})

def traitement_edit(request, pk):
    traitement = get_object_or_404(Traitement, pk=pk)
    if request.method == "POST":
        form = TraitementForm(request.POST, instance=traitement)
        if form.is_valid():
            form.save()
            return redirect('consulter_traitements', consultation_id=traitement.consultation.id)
    else:
        form = TraitementForm(instance=traitement)
    return render(request, 'medico/traitement_form.html', {'form': form})


def liste_urgences(request):
    urgences = Urgence.objects.all().order_by('-date_signalement')
    return render(request, 'medico/liste_urgences.html', {'urgences': urgences})



def signaler_urgence(request, consultation_id):
    consultation = get_object_or_404(Consultation, id=consultation_id)
    
    if request.method == 'POST':
        form = UrgenceForm(request.POST)
        if form.is_valid():
            urgence = form.save(commit=False)
            urgence.consultation = consultation
            urgence.save()
            return redirect('liste_urgences')
    else:
        form = UrgenceForm()

    return render(request, 'medico/signal_urgence.html', {
        'form': form,
        'consultation': consultation
    })


def marquer_traitee(request, urgence_id):
    urgence = get_object_or_404(Urgence, id=urgence_id)
    urgence.traitee = True
    urgence.save()
    return redirect('liste_urgences')



def supprimer_urgence(request, urgence_id):
    urgence = get_object_or_404(Urgence, id=urgence_id)
    urgence.delete()
    return redirect('liste_urgences')


