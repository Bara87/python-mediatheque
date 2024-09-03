from django.test import TestCase
from django.urls import reverse
from .models import Emprunteur, Media, Emprunt

class MenuViewTests(TestCase):
    def test_menu_view(self):
        response = self.client.get(reverse('bibliothecaire_menu'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Menu Bibliothécaire")

class MembreViewTests(TestCase):
    def test_liste_membres_view(self):
        Emprunteur.objects.create(nom="Test Membre")
        response = self.client.get(reverse('membres'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Membre")

    def test_ajout_membre_view(self):
        response = self.client.post(reverse('ajout_membre'), {'nom': 'Nouveau Membre'})
        self.assertEqual(response.status_code, 302)  # Redirection après succès
        self.assertTrue(Emprunteur.objects.filter(nom='Nouveau Membre').exists())

class MediaViewTests(TestCase):
    def test_liste_medias_view(self):
        Media.objects.create(nom="Test Media", disponible=True)
        response = self.client.get(reverse('medias'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Media")

    def test_ajout_media_view(self):
        response = self.client.post(reverse('ajouter_media'), {'type_media': 'livre', 'nom': 'Nouveau Livre'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Media.objects.filter(nom='Nouveau Livre').exists())

class EmpruntViewTests(TestCase):
    def test_liste_emprunts_view(self):
        emprunteur = Emprunteur.objects.create(nom="Test Membre")
        media = Media.objects.create(nom="Test Media", disponible=True)
        Emprunt.objects.create(emprunteur=emprunteur, media=media)
        response = self.client.get(reverse('emprunts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Membre")
        self.assertContains(response, "Test Media")

    def test_ajout_emprunt_view(self):
        emprunteur = Emprunteur.objects.create(nom="Test Membre")
        media = Media.objects.create(nom="Test Media", disponible=True)
        response = self.client.post(reverse('ajouter_emprunt'), {'media': media.id, 'emprunteur': emprunteur.id})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Emprunt.objects.filter(emprunteur=emprunteur, media=media).exists())
