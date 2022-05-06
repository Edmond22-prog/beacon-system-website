from django.shortcuts import render
from django.views.generic import TemplateView


class Accueil(TemplateView):
    template_name = "website/accueil.html"


class Contact(TemplateView):
    template_name = "website/contact.html"


class Developpement(TemplateView):
    template_name = "website/developpement.html"


class Hebergement(TemplateView):
    template_name = "website/hebergement.html"


class Marketing(TemplateView):
    template_name = "website/marketing.html"
