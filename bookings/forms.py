# from django import forms
# from datetime import datetime


# class BookingForm(forms.Form):

#     GUEST_NUM_CHOICES = (
#         (1, '1'),
#         (2, '2'),
#     )

#     checkin_date = forms.DateField(
#         required=True,
#         widget=forms.DateInput(
#             attrs={'type': 'date', 'min': datetime.now().date}
#         )
#     )
#     checkout_date = forms.DateField(
#         required=True,
#         widget=forms.DateInput(
#             attrs={'type': 'date', 'min': datetime.now().date}
#         )
#     )
#     total_guests = forms.IntegerField(
#         choices=GUEST_NUM_CHOICES, default=1, required=True)
#     guest_firstname = forms.CharField(max_length=50, required=True)
#     guest_surname = forms.CharField(max_length=50, required=True)
#     guest_email = forms.EmailField(required=True)


from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ["total_guests", "guest_firstname", "guest_surname",
                  "guest_email", "checkin_date", "checkout_date", "guest_request"]
