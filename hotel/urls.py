from django.urls import path
from . import views
from .views import hotel_list, room_list, book_room, booking_confirmation, add_review_rating, review_confirmation

app_name = 'hotel'

urlpatterns = [
    path('hotel_list/', hotel_list, name='hotel_list'),
    path('room_list/<int:hotel_id>/', views.room_list, name='room_list'),
    path('book_room/<int:room_id>/', views.book_room, name='book_room'),
    path('booking_confirmation/', booking_confirmation, name='booking_confirmation'),
    path('add_review_rating/', add_review_rating, name='add_review_rating'),
    path('review_confirmation/', review_confirmation, name='review_confirmation'),
]
