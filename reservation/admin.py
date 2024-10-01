from django.contrib import admin
from .models import Reservation

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """
    Allows admins a quick overview of all bookings,
    with the ability to filter by date and time for a precise overview.
    intended for use when seating walk-in customers on a given day or
    making business decsions. Also allows for search by booking lead.

    Containts methods to accept or decline the bookings within the dropdown.
    """
    list_display = ('lead', 'date', 'time', 'guests', 'status',)
    list_filter = ('date', 'time',)
    search_fields = ('lead',)
    actions = ['accept_booking', 'decline_booking']