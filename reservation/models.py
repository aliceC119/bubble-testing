from django.db import models
from django.contrib.auth.models import User

# A tuple to hold the status key for the Booking model.
STATUS = ((0, "pending"), (1, "accepted"), (2, "declined"))

# Create your models here.
class Reservation(models.Model):
    """
    The model for the booking app.

    Inherits the user from account sign up.
    Stores the booking: lead, email, mobile, date, time
    and how many guests for each individual booking.
    Plus any special requirement notes.

    Defaults the booking status to 'pending' using the above tuple.

    Validation for the mobile field is handled with Django's inbuilt
    RegexValidator.
    """
    # Foreign Key from the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # User Info needed for Booking
    lead = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, blank=False)
    # Contact Number for Booking & Validator
    
    # Date of Booking
    date = models.DateField(blank=False)
    # Time of Booking
    time = models.TimeField(blank=False)
    # Special Requests for Booking
    notes = models.TextField(max_length=200)
    # Number of Guests on Booking
    guests = models.PositiveIntegerField(blank=False)
    # Booking Status - status updates handled in admin
    status = models.IntegerField(choices=STATUS, default=0)