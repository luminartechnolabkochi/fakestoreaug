from django import forms
from django.contrib.auth.models import  User

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

# ModelForm
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password"]