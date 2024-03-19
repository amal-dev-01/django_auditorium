# forms.py
from django import forms
from .models import Event, RoomType,EventPrice,Booking
from django.utils import timezone
from django.core.exceptions import ValidationError



class BookingForm(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=Event.objects.all())
    room_type = forms.ModelChoiceField(queryset=RoomType.objects.all())
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': timezone.now().strftime('%Y-%m-%d')}   )
    )
    time =forms.TimeField(
    widget=forms.TimeInput(attrs={'type': 'time'})
  
    )

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < timezone.now().date():
            raise ValidationError("You cannot book a date in the past.")
        return date

    class Meta:
        model = Booking
        fields = ['event','room_type','date', 'time', 'user', 'description', 'discount', 'advance']


class BookingStatusForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status','balance']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
