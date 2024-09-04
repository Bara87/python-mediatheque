from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='bibliothecaire_menu'),  # Page d'accueil
    path('membres/', views.membres, name='membres'),  # Liste des membres
    path('medias/', views.medias, name='medias'),  # Liste des médias
    path('emprunts/', views.emprunts, name='emprunts'),  # Liste des emprunts
    path('ajouter-emprunt/', views.ajouter_emprunt, name='ajouter_emprunt'),  # Formulaire pour ajouter un emprunt
    path('ajout-membre/', views.ajout_membre, name='ajout_membre'),  # Formulaire pour ajouter un membre
    path('ajouter_media/', views.ajouter_media, name='ajouter_media'), 
    path('membres/<int:membre_id>/mettre_a_jour/', views.mettre_a_jour_membre, name='mettre_a_jour_membre'),
    path('membres/<int:membre_id>/supprimer/', views.supprimer_membre, name='supprimer_membre'),
    path('membres/<int:emprunter_id>/afficher/', views.afficher_membre, name='afficher_membre'),
     path('emprunt/<int:emprunt_id>/supprimer/', views.supprimer_emprunt, name='supprimer_emprunt'),
]