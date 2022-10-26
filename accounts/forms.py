from django import forms
from django.forms import ModelForm

from myprint.models import User



class UserLoginForm(forms.Form):
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": 'form-control mb-2 form-control',
        'type': 'number',
        'placeholder': 'Телефон ...'
    }))
    password = forms.CharField(max_length=20,widget=forms.TextInput(attrs={
        "class": 'form-control mb-5',
        'type': 'pasword',
        'placeholder': 'Пароль ...'
    }))
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
