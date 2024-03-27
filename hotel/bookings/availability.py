import datetime
from hotel.models import room, booking



def check_availability(rooms,check_in,check_out):
    available=[]
    Booking = booking.objects.filter(rooms=rooms)
    for bookingss in Booking:
        if bookingss.check_in>check_out or bookingss.check_out<check_in:
            available.append(True)
        else:
            available.append(False)
            
    return all(available)