from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Booking

def home(request):
    return render(request, 'home/home.html')

def home(request):
    return render(request, 'bookings/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings.html', {'bookings': user_bookings})


# bookings/views.py
from django.shortcuts import render
from .models import Booking

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})
