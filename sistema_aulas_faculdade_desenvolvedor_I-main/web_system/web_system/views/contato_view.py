from ..forms import ContactForm
from django.views import View
from django.shortcuts import render

class ContatoView(View):
    @staticmethod
    def get(request):
        form = ContactForm()
        context = {
            'form':form,
            'url_form': 'class_contact',
        }

        return render(request, 'contact/contact.html', context)
    
    @staticmethod
    def post(request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            sender = form.cleaned_data.get("sender")
            cc_myself = form.cleaned_data.get("cc_myself")
            print("Subject", subject)
            recipients = ['']
            if cc_myself:
                recipients.append(sender)
            context = {
                'recipients': recipients,
                'form': form,
            }