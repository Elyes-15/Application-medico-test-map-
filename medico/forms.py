from django import forms
from .models import Consultation

class ConsultationForm(forms.ModelForm):
      class Meta:
        model = Consultation
        fields = ['patient_nom', 'patient_prenom', 'patient_genre', 'patient_age', 'description']