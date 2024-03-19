from django.shortcuts import render,redirect
from home.forms import StaffRegistrationForm,UserRegisterForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login,logout
from booking.models import Booking
from django.http import HttpResponseNotFound
from booking.forms import BookingStatusForm

# Create your views here.
@login_required(login_url="login/")
def home(request):
    return render(request,'home.html')

def staff_register(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.instance.is_verified =True
            form.instance.is_staff =True
            form.save()
            return redirect('admin_home')  
    else:
        form = StaffRegistrationForm()
    return render(request, 'staff_register.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.instance.is_verified =True
            form.instance.is_staff =False
            form.save()
            return redirect('/')  
    else:
        form = UserRegisterForm()
    
    return render(request, 'user_register.html', {'form': form})



def staff_login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                if user.is_admin:
                    login(request, user)
                    return redirect('admin_home')
                elif user.is_staff:
                    login(request, user)
                    return redirect('/')

            else:
                error_message = "Invalid username or password. Please try again."
                return render(request, 'login.html', {'error_message': error_message})
            
        except Exception as e:
            pass
    
    return render(request, 'login.html')


def staff_logout(request):
    logout(request)
    return redirect('login')


def admin_booking(request):
    bookings=Booking.objects.all()
    return render(request,'booking_list.html',{'bookings':bookings})


def admin_booking_detail(request, id):
    try:
        booking = Booking.objects.get(id=id)
    except Booking.DoesNotExist:
        return HttpResponseNotFound("Booking not found")

    if request.method == 'POST':
        form = BookingStatusForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_detail', id=id)
    else:
        form = BookingStatusForm(instance=booking)
    return render(request, 'booking_details.html', {'booking': booking, 'form': form})


@login_required(login_url="login/")
def admin_home(request):
    wedding_count = Booking.objects.filter(event_price__event=1).count()
    birthday_count = Booking.objects.filter(event_price__event=2).count()
    party_count = Booking.objects.filter(event_price__event=3).count()
    context = {
        'wedding_count': wedding_count,
        'birthday_count': birthday_count,
        'party_count': party_count,
    }
    return render(request,'adminhome.html',context)