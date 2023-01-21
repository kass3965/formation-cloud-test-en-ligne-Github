
from django.contrib import admin
from django.urls import path

from Emargement.views import emargement, emargement_list

urlpatterns = [
path('', emargement, name= 'emargement'),
path('emargement_list', emargement_list, name= 'emargement_list'),
path('admin/', admin.site.urls),
]
