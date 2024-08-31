from django import forms
from .models import *


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Buy
        exclude = ['product']
        fields = '__all__'


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = '__all__'
        exclude = ['massege']

class ContactForm(forms.ModelForm):


    class Meta:
        model = Register
        fields = '__all__'
        exclude = ['password', 'Lastname', 'phone']
