from django.shortcuts import render, redirect
from .models import FitnessClass, Booking
from django.contrib.auth.decorators import login_required

def class_list(request):
    classes = FitnessClass.objects.all()
    return render(request, 'booking/class_list.html', {'classes': classes})


@login_required
def book_class(request, class_id):
    fitness_class = FitnessClass.objects.get(id=class_id)
    
    if Booking.objects.filter(user=request.user, fitness_class=fitness_class).exists():
        return redirect('class_list')

    Booking.objects.create(user=request.user, fitness_class=fitness_class)
    return redirect('class_list')

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})
