from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ["total_guests", "guest_firstname", "guest_surname",
                  "guest_email", "checkin_date", "checkout_date", "guest_request"]
