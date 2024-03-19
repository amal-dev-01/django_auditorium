from django.contrib import admin

# Register your models here.
from booking.models import Event,Booking,RoomType,EventPrice


admin.site.register(Event)
admin.site.register(Booking)
admin.site.register(RoomType)
admin.site.register(EventPrice)