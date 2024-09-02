from django.db import models
from django.utils import timezone
from datetime import timedelta

class Emprunteur(models.Model):
    nom = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} - {'Bloqué' if self.bloque else 'Actif'}"

    def peut_emprunter(self):
        if self.bloque:
            return False
        # Vérifie s'il a des emprunts en retard
        emprunts_en_retard = Emprunt.objects.filter(emprunteur=self, date_retour__isnull=True, date_emprunt__lt=timezone.now() - timedelta(days=7))
        if emprunts_en_retard.exists():
            return False
        return True

    def emprunts_actuels(self):
        return Emprunt.objects.filter(emprunteur=self, date_retour__isnull=True).count()

class Media(models.Model):
    nom = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    date_emprunt = models.DateTimeField(null=True, blank=True)
    date_retour = models.DateTimeField(null=True, blank=True)
    emprunteur = models.ForeignKey(Emprunteur, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.nom} - {'Disponible' if self.disponible else 'Non disponible'}"

    def est_disponible_pour_emprunt(self):
        return self.disponible and not isinstance(self, JeuDePlateau)

    def est_en_retard(self):
        if self.date_retour:
            return self.date_retour < timezone.now()
        return self.date_emprunt and timezone.now() > self.date_emprunt + timedelta(days=7)

    def save(self, *args, **kwargs):
        if self.date_retour:
            self.disponible = True
        else:
            self.disponible = False
        super().save(*args, **kwargs)

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

class Emprunt(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour = models.DateTimeField(null=True, blank=True)

    def est_en_retard(self):
        if self.date_retour:
            return self.date_retour < timezone.now()
        return timezone.now() > self.date_emprunt + timedelta(days=7)