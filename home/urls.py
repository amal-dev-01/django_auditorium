from django.urls import path
from home.views import staff_register,home,user_register,staff_login,staff_logout,admin_booking,admin_home,admin_booking_detail

urlpatterns = [
    path('', home,name='home'),
    path('register/', staff_register,name='staff_register'),
    path('user/register/', user_register,name='user_register'),
    path('login/', staff_login,name='login'),
    path('logout/', staff_logout,name='logout'),

    
    path('adminpage/list/', admin_booking,name='booking_list'),
    path('adminpage/home/', admin_home,name='admin_home'),
    path('adminpage/booking/<int:id>/', admin_booking_detail,name='booking_detail'),



    
]