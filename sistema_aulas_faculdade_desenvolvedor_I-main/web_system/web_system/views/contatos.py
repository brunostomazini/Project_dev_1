from django.shortcuts import render
from ..forms import ContactForm


def contact(request):
    if request.method == 'GET':
        form = ContactForm(request.POST)
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        sender = form.cleaned_data.get("sender")
        cc_myself = form.cleaned_data.get("cc_myself")

        recipients = ['ricardo.santos@restinga.ifrs.edu.br']
        if cc_myself:
            recipients.append(sender)

        ##

            context = {
                'recipients' : recipients,
                'form' : form,
            }
            return render(request, 'contact/thanks.html', context)

        context = {'form': form,
        'url_form': 'function_contato',
        }
        return render(request, 'contact/contact.html', context)

    elif request.method == "GET":
        form = ContactForm()
        context = {
            'form' : form,
            'url_form' : "function_contact"
        }
        return render(request, 'contact/contact.html', context)
    





