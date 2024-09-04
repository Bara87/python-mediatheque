# membres/views.py
from django.shortcuts import render
from .models import Livre, DVD, CD, JeuDePlateau



def menu(request):
    return render(request, 'membre/menu.html')

def liste_medias(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux = JeuDePlateau.objects.all()

    context = {
        'livres': livres,
        'dvds': dvds,
        'cds': cds,
        'jeux': jeux,
    }

    return render(request, 'membre/liste_medias.html', context)