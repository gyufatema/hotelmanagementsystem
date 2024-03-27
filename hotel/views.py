from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Hotel, room, booking, ReviewRating

@login_required
def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})

@login_required
def room_list(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    rooms = room.objects.filter(hotel=hotel)
    return render(request, 'room_list.html', {'hotel': hotel, 'rooms': rooms})

@login_required
def book_room(request, room_id):
    room = get_object_or_404(room, pk=room_id)
    if request.method == 'POST':
        # Process form submission
        # Assuming you have form fields in the HTML form with appropriate names
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        # Create booking object
        booking = booking.objects.create(
            user=request.user,
            room=room,
            hotel=room.hotel,
            check_in=check_in,
            check_out=check_out
        )
        return redirect('booking_confirmation')
    else:
        return render(request, 'book_room.html', {'room': room})

@login_required
def booking_confirmation(request):
    bookings = booking.objects.filter(user=request.user)
    return render(request, 'booking_confirmation.html', {'bookings': bookings})

@login_required
def add_review_rating(request, hotel_id=None, room_id=None):
    if hotel_id:
        obj = get_object_or_404(Hotel, pk=hotel_id)
    elif room_id:
        obj = get_object_or_404(room, pk=room_id)
    if request.method == 'POST':
        # Process form submission
        # Assuming you have form fields in the HTML form with appropriate names
        stars = request.POST.get('stars')
        feedback = request.POST.get('feedback')
        # Create review or rating object
        ReviewRating.objects.create(
            user=request.user,
            hotel=obj if hotel_id else obj.hotel,
            room=obj if room_id else None,
            stars=stars,
            feedback=feedback
        )
        return redirect('review_confirmation')
    else:
        return render(request, 'add_review_rating.html', {'obj': obj})

@login_required
def review_confirmation(request):
    return render(request, 'review_confirmation.html')
