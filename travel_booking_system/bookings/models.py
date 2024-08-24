from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)
    travel_date = models.DateField()
    return_date = models.DateField()
    # Add more fields as needed

    def __str__(self):
        return f"Booking by {self.user} to {self.destination}"

