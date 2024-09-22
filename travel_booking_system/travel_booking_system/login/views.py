# login/views.py

from django.shortcuts import render

def login_view(request):
    return render(request, 'login/index.html')  # Adjust the template name as needed
