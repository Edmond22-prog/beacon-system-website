from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView, View
from .models import Testimonial
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail.message import BadHeaderError
from django.utils.html import format_html


class HomeView(TemplateView):
    template_name = "website/home.html"
    
    def get(self, request, *args, **kwargs):
        testimonials = Testimonial.objects.all()
        context = {
            'nbar': 'home',
            'testimonials': testimonials
        }
        return render(request, self.template_name, context)
    

# class Services(TemplateView):
#     template_name = "website/services.html"
    
#     def get(self, request, *args, **kwargs):
#         context = {
#             'nbar': 'services',
#         }
#         return render(context, self.template_name, context)
    
    
class DevelopmentView(TemplateView):
    template_name = "website/development.html"
    
    def get(self, request, *args, **kwargs):
        context = {
            'nbar': 'services',
        }
        return render(context, self.template_name, context)


class HostingView(TemplateView):
    template_name = "website/hosting.html"
    
    def get(self, request, *args, **kwargs):
        context = {
            'nbar': 'services',
        }
        return render(context, self.template_name, context)


class MarketingView(TemplateView):
    template_name = "website/marketing.html"

    def get(self, request, *args, **kwargs):
        context = {
            'nbar': 'services',
        }
        return render(context, self.template_name, context)


class ContactView(View):
    form_class = ContactForm
    initial = {'key': 'value'}
    template_name = 'website/contact.html'

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


class ProductView(TemplateView):
    template_name = "website/product.html"
    
    def get(self, request, *args, **kwargs):
        context = {
            'nbar': 'product',
        }
        return render(context, self.template_name, context)