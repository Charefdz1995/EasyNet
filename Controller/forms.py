from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"E-mail","name":"email","type":"email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password","name":"password","type":"password","value":""}))
