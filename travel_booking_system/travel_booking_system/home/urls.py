from django.urls import path
from .views import home_view
from . import views
from .views import create_booking, booking_confirmation, register, login_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', views.about, name='about'),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('book/', create_booking, name='create_booking'),
    path('booking-confirmation/', booking_confirmation, name='booking_confirmation'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
]

urlpatterns += [
    path('book/', create_booking, name='create_booking'),
]