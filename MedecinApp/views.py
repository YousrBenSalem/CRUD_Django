from django.shortcuts import render
from django.views.decorators.csrf import  csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import  JsonResponse

from MedecinApp.models import Medecin , Clinic
from MedecinApp.serializers import ClinicSerializer ,MedecinSerializer

from django.core.files.storage import default_storage



# Create your views here.
@csrf_exempt
def  clinicApi(request , id=0):
  if request.method=='GET':
    clinic = Clinic.objects.all()
    clinic_serializer = ClinicSerializer (clinic, many=True)
    return JsonResponse(clinic_serializer.data , safe=False)
  elif request.method == 'POST':
    clinic_data = JSONParser().parse(request)
    clinic_serializer = ClinicSerializer (data = clinic_data)
    if  clinic_serializer.is_valid():
      clinic_serializer.save()
      return JsonResponse("Added Successfully" , safe=False)
    return JsonResponse("Failed to Add",safe=False)
  elif request.method == 'PUT':
    clinic_data = JSONParser().parse(request)
    clinic = Clinic.objects.get(ClinicId = clinic_data[ "ClinicId"])
    clinic_serializer = ClinicSerializer (clinic , data = clinic_data)
    if  clinic_serializer.is_valid():
      clinic_serializer.save()
      return JsonResponse("Updated Successfully" , safe=False)
    return JsonResponse("Failed to update")
  elif request.method =='DELETE':
    clinic = Clinic.objects.get(ClinicId = id )
    clinic.delete()
    return JsonResponse ("Deleted Successfully" , safe=False)

@csrf_exempt
def medecinApi(request , id=0):
    if request.method =='GET':
      medecin = Medecin.objects.all()
      medecin_serializer = MedecinSerializer (medecin, many=True)
      return JsonResponse(medecin_serializer.data , safe=False)
    elif request.method == 'POST':
      medecin_data = JSONParser().parse(request)
      medecin_serializer = MedecinSerializer (data = medecin_data)
      if medecin_serializer.is_valid():
        medecin_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
      return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
      medecin_data = JSONParser().parse(request)
      medecin = Medecin.objects.get(MedecinId = medecin_data[ "MedecinId"])
      medecin_serializer = MedecinSerializer (medecin , data = medecin_data)
      if  medecin_serializer.is_valid():
        medecin_serializer.save()
        return JsonResponse("Updated Successfully" , safe=False)
      return JsonResponse("Failed to update")
    elif request.method =='DELETE':
      medecin = Medecin.objects.get(MedecinId = id )
      medecin.delete()
      return JsonResponse ("Deleted Successfully" , safe=False)
@csrf_exempt
def SaveFile(request):
    if 'file' in request.FILES:
        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)
        return JsonResponse(file_name, safe=False)
    else:
        return JsonResponse("No file found in request", status=400)