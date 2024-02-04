# contact/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Envoyez l'e-mail (assurez-vous que vos paramètres de messagerie sont configurés correctement)
            subject = 'Nouveau message de contact'
            message = f"Nom: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\n\n{form.cleaned_data['message']}"
            from_email = 'votre@email.com'  # Remplacez par votre adresse e-mail
            to_email = 'destinataire@email.com'  # Remplacez par l'adresse e-mail du destinataire
            send_mail(subject, message, from_email, [to_email])

            return redirect('confirmation_page')  # Redirigez vers une page de confirmation

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
 
