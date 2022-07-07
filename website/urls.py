from django.urls import path
from .views import ContactView, DevelopmentView, HomeView, HostingView, MarketingView, RealisationView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('developpement/', DevelopmentView.as_view(), name='development'),
    path('hebergements/', HostingView.as_view(), name='hosting'),
    path('marketing-digital/', MarketingView.as_view(), name='marketing'),
    path('realisation/', RealisationView.as_view(), name='realisation'),
]
