from django import forms
from django.forms import CharField
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class UserLoginForm(AuthenticationForm):
    username = CharField()
    password = CharField()


    class Meta:
        model = User
        fields = ['username', 'password']