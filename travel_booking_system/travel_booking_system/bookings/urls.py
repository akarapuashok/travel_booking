from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.booking_list, name='booking_list'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('bookings/', views.bookings, name='bookings'),
]
