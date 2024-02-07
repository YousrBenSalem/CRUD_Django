from django.db import models

# Create your models here.
class Clinic(models.Model):
  ClinicId = models.AutoField(primary_key=True)
  ClinicName=models.CharField(max_length=500,null=False)
class Medecin(models.Model):
  MedecinId= models.AutoField(primary_key=True)
  MedecinName=models.CharField(max_length=500)
  Clinic=models.CharField(max_length=500)
  spécialité=models.CharField(max_length=500)
  DateOfJoining=models.DateField()
  photoFileName=models.CharField(max_length=5000)

