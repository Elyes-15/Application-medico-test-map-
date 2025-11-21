from django import forms
from .models import Consultation
from .models import Traitement
from .models import Urgence

class ConsultationForm(forms.ModelForm):
      class Meta:
        model = Consultation
        fields = ['patient_nom', 'patient_prenom', 'patient_genre', 'patient_age', 'description', 'patient_adresse']
        
        

class TraitementForm(forms.ModelForm):
    class Meta:
        model = Traitement
        fields = ['consultation', 'medicament', 'quantite', 'contenant', 'duree_en_jours', 'posologie']

class UrgenceForm(forms.ModelForm):
    class Meta:
        model = Urgence
        fields = ['signes_vitaux', 'remarque']
        widgets = {
            'signes_vitaux': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ex: pouls, tension, respiration...'}),
            'remarque': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Observations du médecin...'}),
        }