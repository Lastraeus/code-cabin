from django.urls import path
from . import views

# urlpatterns = [
#     path('book/', views.BookingFormView.as_view(), name='book')
# ]
urlpatterns = [
    path('book/', views.BookingFormView, name='book')
]
