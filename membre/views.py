from django.shortcuts import render
from bibliothecaire.models import Media

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'membre/menu.html')

def liste_medias(request):
    medias = Media.objects.all()
    return render(request, 'membre/liste_medias.html', {'medias': medias})