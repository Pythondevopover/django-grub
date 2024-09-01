from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Buy
        exclude = ['product']
        fields = '__all__'


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUS
        fields = '__all__'
        exclude = ['password', 'Lastname', 'phone']
