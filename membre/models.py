# membres/models.py
from django.db import models

class Media(models.Model):
    quantite_disponible = models.PositiveIntegerField(default=1)  # Quantité disponible pour emprunt
    nom = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    date_emprunt = models.DateTimeField(null=True, blank=True)
    date_retour = models.DateTimeField(null=True, blank=True)
   

    def __str__(self):
        return f"{self.nom} - {'Disponible' if self.disponible else 'Non disponible'}"

class Livre(Media):
    auteur = models.CharField(max_length=100)

    def __str__(self):
        return f"Livre: {self.nom}, Auteur: {self.auteur}, {'Disponible' if self.disponible else 'Non disponible'}"

class DVD(Media):
    realisateur = models.CharField(max_length=100)

    def __str__(self):
        return f"DVD: {self.nom}, Réalisateur: {self.realisateur}, {'Disponible' if self.disponible else 'Non disponible'}"

class CD(Media):
    artiste = models.CharField(max_length=100)

    def __str__(self):
        return f"CD: {self.nom}, Artiste: {self.artiste}, {'Disponible' if self.disponible else 'Non disponible'}"

class JeuDePlateau(Media):
    createur = models.CharField(max_length=100)

    def __str__(self):
        return f"Jeu de Plateau: {self.nom}, Créateur: {self.createur}, {'Disponible' if self.disponible else 'Non disponible'}"
