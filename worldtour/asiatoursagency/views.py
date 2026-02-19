from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Tour

def index(request):
    tours = Tour.objects.all()
    context = {"tours": tours}
    return render(request, "asiatoursagency/index.html", context)

def home_view(request):
    return render(request, "asiatoursagency/home.html")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()  # Make sure you have this method in your form
            return redirect('success')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'asiatoursagency/contact.html', context)

def success_view(request):
    return render(request, "asiatoursagency/success.html")
