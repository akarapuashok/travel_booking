# register/urls.py

from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    # Add your URL patterns here
    path('', views.register_view, name='register'),
    path('register/', views.register_view, name='register'),
    
]
