from django import forms
from django.forms import ModelForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    fullname = forms.CharField(max_length=255)
    biography = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'fullname', 'biography', 'email', 'password', 'password1', 'password2']