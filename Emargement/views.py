from django.http import HttpResponse
from django.shortcuts import render, redirect

from Emargement.formulaire import EmargementForm
from Emargement.models import Emargement


# Create your views here.
def emargement(request):
    if request.method == 'POST':
        form = EmargementForm(request.POST)
        if form.is_valid():
            emargement = form.save()
            return redirect('emargement')
    else:
        form = EmargementForm()
    return render(request, 'Emargement/Emargement.html', {'form': form})


def emargement_list(request):
    emargements = Emargement.objects.all()
    return render(request, 'Emargement/Emargement_list.html', {'emargements': emargements})


