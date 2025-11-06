from django import forms
from .models import Consultation
from .models import Traitement

class ConsultationForm(forms.ModelForm):
      class Meta:
        model = Consultation
        fields = ['patient_nom', 'patient_prenom', 'patient_genre', 'patient_age', 'description']
        
        

class TraitementForm(forms.ModelForm):
    class Meta:
        model = Traitement
        fields = ['consultation', 'medicament', 'quantite', 'contenant', 'duree_en_jours', 'posologie']
