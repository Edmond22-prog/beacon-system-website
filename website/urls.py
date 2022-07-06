from django.urls import path
from .views import ContactView, DevelopmentView, HomeView, HostingView, MarketingView, PageNotFoundView, RealisationView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('developpement/', DevelopmentView.as_view(), name='development'),
    path('hebergements/', HostingView.as_view(), name='hosting'),
    path('marketing-digital/', MarketingView.as_view(), name='marketing'),
    path('realisation/', RealisationView.as_view(), name='realisation'),
    path('not-found-404/', PageNotFoundView.as_view(), name='not_found'),
]
