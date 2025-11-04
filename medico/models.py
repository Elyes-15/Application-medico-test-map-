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
