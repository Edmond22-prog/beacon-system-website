from django.urls import path

from .views import Accueil, Contact, Developpement, Hebergement, Marketing


urlpatterns = [
    path('', Accueil.as_view(), name='accueil'),
    path('contact/', Contact.as_view(), name='contact'),
    path('services/developpement/', Developpement.as_view(), name='developpement'),
    path('services/hebergement/', Hebergement.as_view(), name='hebergement'),
    path('marketing/', Marketing.as_view(), name='marketing'),
]
