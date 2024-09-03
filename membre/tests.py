from django.test import TestCase
from django.urls import reverse
from bibliothecaire.models import Media

class MembreViewsTestCase(TestCase):
    
    def setUp(self):
        """Prépare les objets nécessaires pour les tests."""
        # Crée un média pour les tests
        self.media = Media.objects.create(nom="Le Grand Livre", disponible=True)
    
    def test_liste_medias_view(self):
        """Teste la vue de la liste des médias."""
        # Effectue une requête GET sur la vue 'liste_medias'
        response = self.client.get(reverse('liste_medias'))
        
        # Vérifie que le code de réponse HTTP est 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Vérifie que le bon template est utilisé
        self.assertTemplateUsed(response, 'membre/liste_medias.html')
        
        # Vérifie que le média créé est affiché dans la réponse
        self.assertContains(response, self.media.nom)