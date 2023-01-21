from django.db import models
from django.contrib import admin

# Create your models here.

class Emargement(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    numero_telephone = models.CharField(max_length=10)
    email = models.EmailField()
    date_inscription = models.DateTimeField(auto_now_add=True)


class EmargementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'numero_telephone','email','date_inscription')
    list_filter = ('date_inscription',)
    search_fields = ['nom','email','numero_telephone']
