from django import forms
from .models import Emprunteur, Livre, DVD, CD, JeuDePlateau

class EmprunteurForm(forms.ModelForm):
    class Meta:
        model = Emprunteur
        fields = ['nom', 'bloque']


class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['nom', 'auteur', 'disponible']

class DVDForm(forms.ModelForm):
    class Meta:
        model = DVD
        fields = ['nom', 'realisateur', 'disponible']

class CDForm(forms.ModelForm):
    class Meta:
        model = CD
        fields = ['nom', 'artiste', 'disponible']

class JeuDePlateauForm(forms.ModelForm):
    class Meta:
        model = JeuDePlateau
        fields = ['nom', 'createur', 'disponible']