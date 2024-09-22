# home/admin.py

from django.contrib import admin
from .models import Destination, Hotel, Flight, Booking
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'description')
    search_fields = ('name', 'country')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'rating', 'price_per_night')
    search_fields = ('name', 'destination__name')
    list_filter = ('destination', 'rating')

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'departure', 'arrival', 'price')
    search_fields = ('flight_number', 'departure', 'arrival')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'destination', 'hotel', 'flight', 'check_in_date', 'check_out_date')
    search_fields = ('user__username', 'destination__name', 'hotel__name', 'flight__flight_number')
    list_filter = ('destination', 'hotel', 'flight', 'check_in_date')



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Define additional fields and configurations here

admin.site.register(CustomUser, CustomUserAdmin)