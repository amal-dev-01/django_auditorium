from django.db import models
from home.models import User
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
    
class RoomType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
    

class EventPrice(models.Model):
    event = models.ForeignKey(Event,on_delete =models.CASCADE)
    room_type = models.ForeignKey(RoomType,on_delete =models.CASCADE)
    price = models.IntegerField()


    def __str__(self):
        return f"{self.event} -{self.room_type} - ${self.price}"
    

class Booking(models.Model):
    PENDING = 'pending'
    CANCELED = 'canceled'
    CONFIRMED = 'confirmed'
    COMPLETED ='completed'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (CANCELED, 'Canceled'),
        (COMPLETED ,'Completed'),
    ]

    date = models.DateField()
    time =models.TimeField()
    user = models.ForeignKey(User,on_delete =models.CASCADE)
    event_price =models.ForeignKey(EventPrice,on_delete =models.CASCADE)
    description =models.TextField()
    discount =models.IntegerField()
    total_price = models.IntegerField()
    advance = models.IntegerField()
    balance =models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)


    def __str__(self):
        return f"{self.event_price} - ${self.total_price}"
 




