import logging
from django.shortcuts import render, redirect, get_object_or_404
from .models import Emprunteur, Media, Emprunt, JeuDePlateau, Livre, CD, DVD
from .forms import EmprunteurForm, LivreForm, DVDForm, CDForm, JeuDePlateauForm

# Configuration du logger
logger = logging.getLogger(__name__)

def menu(request):
    logger.info("Affichage du menu principal du bibliothécaire")
    return render(request, 'bibliothecaire/menu.html')

def membres(request):
    logger.info("Affichage de la liste des membres")
    membres = Emprunteur.objects.all()
    return render(request, 'bibliothecaire/membres.html', {'membres': membres})

def afficher_membre(request, emprunter_id):
    # Récupère l'emprunteur et ses emprunts
    emprunteur = get_object_or_404(Emprunteur, id=emprunter_id)
    emprunts = Emprunt.objects.filter(emprunteur=emprunteur, date_retour__isnull=True)

    # Rendre le template avec les détails de l'emprunteur et ses emprunts
    return render(request, 'bibliothecaire/detail.html', {
        'emprunteur': emprunteur,
        'emprunts': emprunts,
    })

def medias(request):
    livres = Livre.objects.all()
    cds = CD.objects.all()
    dvds = DVD.objects.all()
    jeux = JeuDePlateau.objects.all()
    
    context = {
        'livres': livres,
        'cds': cds,
        'dvds': dvds,
        'jeux': jeux
    }
    return render(request, 'bibliothecaire/medias.html', context)

def emprunts(request):
    logger.info("Affichage de la liste des emprunts")
    emprunts = Emprunt.objects.all()
    return render(request, 'bibliothecaire/emprunts.html', {'emprunts': emprunts})

def ajout_membre(request):
    if request.method == 'POST':
        form = EmprunteurForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info(f"Ajout d'un nouveau membre: {form.cleaned_data['nom']}")
            return redirect('membres')
        else:
            logger.warning("Formulaire d'ajout de membre invalide")
    else:
        form = EmprunteurForm()
        logger.info("Affichage du formulaire d'ajout de membre")
    return render(request, 'bibliothecaire/ajout_membre.html', {'form': form})

def supprimer_membre(request, membre_id):
    membre = get_object_or_404(Emprunteur, id=membre_id)
    logger.info(f"Tentative de suppression du membre: {membre.nom}")
    
    # Vérifiez si le membre a des emprunts non retournés
    emprunts_non_restitues = Emprunt.objects.filter(emprunteur=membre, date_retour__isnull=True)
    
    if emprunts_non_restitues.exists():
        logger.warning(f"Échec de la suppression du membre {membre.nom} car il a des emprunts non retournés")
        return render(request, 'bibliothecaire/error.html', {
            'message': "Impossible de supprimer ce membre car il a des emprunts non retournés."
        })

    if request.method == 'POST':
        membre.delete()
        logger.info(f"Membre supprimé: {membre.nom}")
        return redirect('membres')
    
    logger.info(f"Affichage de la page de confirmation pour la suppression du membre: {membre.nom}")
    return render(request, 'bibliothecaire/confirmation_suppression.html', {'membre': membre})

def ajouter_emprunt(request):
    if request.method == 'POST':
        media_id = request.POST.get('media')
        emprunteur_id = request.POST.get('emprunteur')

        media = get_object_or_404(Media, id=media_id)
        emprunteur = get_object_or_404(Emprunteur, id=emprunteur_id)

        if not emprunteur.peut_emprunter():
            return render(request, 'bibliothecaire/error_media_emprunt.html', {'message': "L'emprunteur ne peut pas emprunter en raison d'emprunts en retard ou de son statut bloqué.", 'error_type': 'emprunt'})

        if emprunteur.emprunts_actuels() >= 3:
            return render(request, 'bibliothecaire/error_media_emprunt.html', {'message': "Un emprunteur ne peut pas avoir plus de 3 emprunts en cours.", 'error_type': 'emprunt'})

        if not media.est_disponible_pour_emprunt():
            return render(request, 'bibliothecaire/error_media_emprunt.html', {'message': "Le média n'est pas disponible ou il s'agit d'un jeu de plateau.", 'error_type': 'media'})

        Emprunt.objects.create(media=media, emprunteur=emprunteur)

        media.quantite_disponible -= 1
        media.save()

        return redirect('emprunts')

    membres = Emprunteur.objects.all()
    medias = Media.objects.exclude(id__in=JeuDePlateau.objects.values_list('id', flat=True))
    return render(request, 'bibliothecaire/ajouter_emprunt.html', {'membres': membres, 'medias': medias})

def supprimer_emprunt(request, emprunt_id):
    if request.method == 'POST':
        emprunt = get_object_or_404(Emprunt, id=emprunt_id)
        emprunter_id = emprunt.emprunteur.id
        emprunt.delete()  # Supprimer l'emprunt
        return redirect('afficher_membre', emprunter_id=emprunter_id)
    return redirect('error_page')  # Page d'erreur si la méthode n'est pas POST


def mettre_a_jour_membre(request, membre_id):
    membre = get_object_or_404(Emprunteur, id=membre_id)
    
    if request.method == 'POST':
        form = EmprunteurForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect('membres')
    else:
        form = EmprunteurForm(instance=membre)
    
    return render(request, 'bibliothecaire/mettre_a_jour_membre.html', {'form': form, 'membre': membre})

def ajouter_media(request):
    if request.method == 'POST':
        type_media = request.POST.get('type_media')

        if type_media == 'livre':
            form = LivreForm(request.POST)
        elif type_media == 'dvd':
            form = DVDForm(request.POST)
        elif type_media == 'cd':
            form = CDForm(request.POST)
        elif type_media == 'jeu_de_plateau':
            form = JeuDePlateauForm(request.POST)
        else:
            form = None

        if form and form.is_valid():
            form.save()
            return redirect('medias')
    else:
        form = LivreForm()  # Affiche le formulaire par défaut, peut-être offrir un choix de type media ici.

    return render(request, 'bibliothecaire/ajouter_media.html', {'form': form})
