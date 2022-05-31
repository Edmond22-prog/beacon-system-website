from django.urls import path

from .views import Home, Contact, Development, Hosting, Marketing, Services

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('contact/', Contact.as_view(), name='contact'),
    path('services/', Services.as_view(), name='services'),
    path('services/developpement/', Development.as_view(), name='realisation'),
    path('services/hebergement/', Hosting.as_view(), name='hosting'),
    path('marketing/', Marketing.as_view(), name='marketing'),
]
