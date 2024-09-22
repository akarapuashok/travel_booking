# login/urls.py

from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.login_view, name='login'), # Add your URL patterns here
    # Example: path('', views.login_view, name='login'),
]
