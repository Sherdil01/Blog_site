from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password kiriting',
                 widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'passwordni kiriting'}))
    password2 = forms.CharField(label='Password qayta kiriting',
                 widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'passwordni qayta kiriting'}))
    
    class Meta:
        model = Account
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Username kiriting'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'email  kiriting'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'phone numberni kiriting'}),
            

        }
        
        
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'data_of_birth', 'image', 'address', ]