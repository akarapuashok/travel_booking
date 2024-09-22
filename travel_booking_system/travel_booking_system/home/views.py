from django.shortcuts import render, redirect
from .forms import BookingForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


def home_view(request):
    return render(request, 'home/index.html')

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def home_view(request):
    return render(request, 'home/home.html')

def about_view(request):
    return render(request, 'home/about.html')

def about(request):
    return render(request, 'home/about.html')



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'home/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_confirmation')  # Redirect to confirmation page
    else:
        form = BookingForm()
    return render(request, 'home/booking_form.html', {'form': form})

def booking_confirmation(request):
    return render(request, 'home/booking_confirmation.html')



print("views.py loaded")  # Add this line at the top




