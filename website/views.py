from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView, View
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail.message import BadHeaderError
from django.utils.html import format_html



class Home(TemplateView):
    # template_name = "website/accueil.html"
    template_name = "updated/home.html"
    
    def get(self, request, *args, **kwargs):
        context = {
            'nbar': 'home',
        }
        return render(request, self.template_name, context)
    

class Services(TemplateView):
    # template_name = "website/developpement.html"
    template_name = "updated/services.html"
    
    def get(self, request, *args, **kwargs):
        context = {
            'nbar': 'services',
        }
        return render(context, self.template_name, context)
    
    
class Development(TemplateView):
    # template_name = "website/developpement.html"
    template_name = "updated/services.html"
    
    def get(self, request, *args, **kwargs):
        context = {
            'nbar': 'services',
        }
        return render(context, self.template_name, context)


class Hosting(TemplateView):
    # template_name = "website/hebergement.html"
    template_name = "updated/realisation.html"
    
    def get(self, request, *args, **kwargs):
        context = {
            'nbar': 'services',
        }
        return render(context, self.template_name, context)


class Marketing(TemplateView):
    template_name = "website/marketing.html"


class Contact(View):
    form_class = ContactForm
    initial = {'key': 'value'}
    template_name = 'updated/contact.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {
            'form': form,
            'nbar' : 'contact',
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            emailSubject = f'{name} <{email}>: ' + f'{subject}'

            # Uncomment this later to send email to required address
            # try:
            #     send_mail(
            #         emailSubject, #subject
            #         message, #message
            #         email, #from email
            #         ['abc@xyz.com'], #to email
            #         fail_silently=False
            #         )
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found')

            # Test if form data was saved and output corresponding flash message to confirm message placement or not.
            try:
                form.save()
                message_out_success = format_html(
                    f'Merci de nous avoir contacter, <strong> {name} </strong> ! Votre message a bien ete envoye. Nous vous joindrons a l\'adresse <strong> {email} </strong> dans les brefs delai.'
                )
                messages.success(
                    request,
                    message_out_success
                )
            except:
                message_out_error = format_html(
                   f'Desole, <strong> {name} </strong> ! Votre message n\'a pas ete envoye. REchargez la page et essayer a nouveau.'
                )
                messages.error(
                    request,
                    message_out_error
                )
            
            # Redidrect to the same page with message output.
            return redirect('contact')
        else:
            form = ContactForm()

        context = {
            'form': form
        }
        return render(request, self.template_name, context)
