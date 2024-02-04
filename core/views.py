from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from contact.forms import ContactForm
from django.core.mail import send_mail



def index(request):
    items = Item.objects.filter(is_sold=False) [0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items,
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Exemple : Enregistrez les données dans la base de données
            form.save()

            # Envoyez un e-mail en utilisant les données du formulaire
            subject = 'Nouveau message de contact'
            message = f"Nom: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\n\n{form.cleaned_data['message']}"
            from_email = form.cleaned_data['email']  
            to_email = 'youssef20ben@gmail.com' 
            send_mail(subject, message, from_email, [to_email])

           

            return render(request, 'core/contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})

def confirmation_page(request):
    # La logique de la vue confirmation_page
    return render(request, 'core/contact_success.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()


    return render(request, 'core/signup.html', {
        'form' : form
    })