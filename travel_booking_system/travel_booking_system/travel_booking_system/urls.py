# travel_booking_system/urls.py
from django.contrib import admin
from django.urls import path, include
from home import views as home_views  # Import your home views if in separate app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),  # Add this line for root URL
    path('bookings/', include('bookings.urls')),
    path('login/', include('login.urls')),  # Assuming login URLs are in login app
    path('register/', include('register.urls')),  # Assuming register URLs are in register app
    path('', include('home.urls')),
    path('login/', include('login.urls')),
    path('register/', include('register.urls')),
    path('', include('home.urls')),
]
