from django.shortcuts import render, redirect
from .models import Course, Registration, ContactMessage
from .forms import RegistrationForm, ContactForm

def home(request):
    courses = Course.objects.all()[:3]
    return render(request, 'homepage.html', {'courses': courses})

def courses(request):
    return render(request, 'courses.html', {'courses': Course.objects.all()})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
