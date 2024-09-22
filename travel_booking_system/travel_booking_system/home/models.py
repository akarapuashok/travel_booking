# home/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True,
    )



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    

    class Category(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)  # Indented
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Indented
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Indented
    stock = models.PositiveIntegerField()  # Indented
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
    
# home/models.py

from django.db import models

class ExampleModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

    def method(self):
        return self.field1

class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Flight(models.Model):
    flight_number = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.flight_number

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='home_bookings')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    booking_date = models.DateField()

    def __str__(self):
        return f'Booking by {self.user.username} for {self.destination.name}'
