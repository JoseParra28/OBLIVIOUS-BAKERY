from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True, help_text='Type a valid email adreess please!')
    
    class Meta():
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2']

