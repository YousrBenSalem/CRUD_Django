from rest_framework import serializers 
from MedecinApp.models import Clinic , Medecin

class ClinicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Clinic
    fields=('ClinicId' ,'ClinicName')
class MedecinSerializer(serializers.ModelSerializer):
  class Meta:
    model = Medecin
    fields=('MedecinId' ,'MedecinName' , 'Clinic' , 'spécialité','DateOfJoining','photoFileName')