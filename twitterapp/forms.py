from django import forms
from django.contrib.auth.forms import UserCreationForm
from twitterapp.models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = [
            "first_name",
            "last_name",
            "age",
        ]