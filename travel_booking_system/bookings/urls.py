from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_booking, name='create_booking'),
    path('list/', views.booking_list, name='booking_list'),
]
