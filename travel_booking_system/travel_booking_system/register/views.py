from django.shortcuts import render, redirect
from .forms import RegisterForm  # Ensure your form is correctly imported

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Adjust the redirect to your actual login URL
    else:
        form = RegisterForm()
    return render(request, 'register/index.html', {'form': form})  # Point to the correct template

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page or any other page
    else:
        form = RegisterForm()
    return render(request, 'register/index.html', {'form': form})
