from django.urls import path
from MedecinApp import views

from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
  path('clinic',views.clinicApi),
  path('clinic/<int:id>',views.clinicApi),  
  path('medecin',views.medecinApi),
  path('medecin/<int:id>',views.medecinApi),  
  path('medecin/savefile',views.SaveFile),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
