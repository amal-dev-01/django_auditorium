from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required  
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Event, RoomType, EventPrice, Booking
from .forms import BookingForm


def get_price(request):
    if request.method == 'GET':
        event_id = request.GET.get('event')
        room_type_id = request.GET.get('room_type')
        try:
            event_price = EventPrice.objects.get(event_id=event_id, room_type_id=room_type_id)
            price = event_price.price
            return JsonResponse({'price': price})
        except EventPrice.DoesNotExist:
            return JsonResponse({'price': None})
    else:
        return HttpResponseBadRequest()
    


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            event = form.cleaned_data['event']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            room_type = form.cleaned_data['room_type']
            discount = form.cleaned_data['discount']
            description = form.cleaned_data['description']
            advance = form.cleaned_data['advance']
            user = form.cleaned_data['user']


            event= EventPrice.objects.filter(event=event, room_type=room_type).first()
            price = event.price
            discount_amount = price * (discount / 100)
            discounted_price = price - discount_amount
            booking=Booking.objects.create(
                date=date,
                time=time,
                user=user,
                event_price=event,
                discount=discount,
                total_price =discounted_price,
                description=description,
                advance=advance,
                balance=discounted_price - advance
            )
            booking.save()
            return redirect('confirmation',booking.id) 
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})


def bookingConfirmation(request,id):
    try:
        booking = Booking.objects.get(id=id)
        return render(request, 'confirmation.html', {'booking': booking})

    except Booking.DoesNotExist:
        return render(request, 'confirmation.html', {'error_message': 'Booking not found'})



def bookinglist(request):
    bookings = Booking.objects.all()
    return render(request, 'bookinglist.html', {'booking': bookings})

