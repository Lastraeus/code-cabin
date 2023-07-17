from django.shortcuts import render, HttpResponseRedirect
from .forms import BookingForm

def BookingFormView(request):

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            # dont commit the object to the database as we need to set the user
            object = form.save(commit=False)
            # set the user
            object.user = request.user
            # finally save the object now that the user has been set
            object.save()

            return HttpResponseRedirect('/')
    else:
        form = BookingForm()

    context = {
        'form': form
    }
    return render(request, 'bookings/book.html', context)
