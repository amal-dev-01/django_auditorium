from django.contrib import admin

# Register your models here.

from home.models import User,Auditorium_Info


admin.site.register(User)
admin.site.register(Auditorium_Info)

