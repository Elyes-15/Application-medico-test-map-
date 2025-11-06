from django.db import models

class Consultation(models.Model):
    patient_nom = models.CharField(max_length=40, null=False)
    patient_prenom = models.CharField(max_length=30, null=False)
    patient_genre = models.CharField(
    max_length=10,
    choices=[('M', 'Homme'), ('F', 'Femme')],
    null=False
    )
    patient_age = models.PositiveIntegerField(null=False)
    description = models.TextField(null=False)
    date_consultation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_prenom} {self.patient_nom} - {self.date_consultation}"
class Traitement(models.Model):
    consultation = models.ForeignKey(
        'Consultation',     
        on_delete=models.CASCADE,  
        related_name='traitements' 
    )
    medicament = models.CharField(max_length=100, null=False)
    quantite = models.PositiveIntegerField(null=False)
    contenant = models.CharField(max_length=50, null=False)
    duree_en_jours = models.PositiveIntegerField(null=False)
    posologie = models.TextField(null=False) 

    def __str__(self):
        return f"{self.medicament} ({self.consultation})"
