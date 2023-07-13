from django.db import models
import datetime
from django.contrib.auth.models import User


class Booking(models.Model):
    """Booking Instance model"""

    GUEST_NUM_CHOICES = (
        (1, '1'),
        (2, '2'),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings_made", )
    total_guests = models.IntegerField(choices=GUEST_NUM_CHOICES, default=1)
    guest_firstname = models.CharField(max_length=50, null=False,  blank=False)
    guest_surname = models.CharField(max_length=50, null=False,  blank=False)
    guest_email = models.EmailField(null=False, blank=False)
    checkin_date = models.DateField(null=False, blank=False)
    checkout_date = models.DateField(null=False, blank=False)
    guest_request = models.CharField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} | Check-In: {self.checkin_date} | Check-out: {self.checkout_date} | Total Guests: {self.total_guests}'

    class Meta:
        ordering = ["-created_on"]
