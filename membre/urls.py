from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.menu, name='membre_menu'),
    path('medias/', views.liste_medias, name='liste_medias'),
]