from django.urls import path
from .views import booking,get_price,bookingConfirmation,bookinglist

urlpatterns = [
    path('book/', booking, name='get_price'),
    path('booking/get_price/', get_price, name='get_price'),
    path('confirmation/<int:id>/', bookingConfirmation, name='confirmation'),
    path('booking_list/', bookinglist, name='bookings'),    
    
]