from django import forms
from .models import Emargement

class EmargementForm(forms.ModelForm):
    class Meta:
        model = Emargement
        fields = ['nom', 'prenom', 'numero_telephone', 'email']

