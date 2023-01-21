from django.contrib import admin

from Emargement.models import Emargement, EmargementAdmin

# Register your models here.
admin.site.register(Emargement,EmargementAdmin)