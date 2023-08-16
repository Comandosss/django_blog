from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=30, required=True,
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': 'Password'}))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
