from django import forms
from .models import User

class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password','first_name','last_name','is_verified']
    
    def save(self, commit=True):
        user = super().save(commit=False) 
        user.set_password(self.cleaned_data["password"])  
        if commit:
            user.save()
        return user


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','phone']
