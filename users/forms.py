from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # built in user model
from .models import Profile


# Using Django built in user form creation
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()  # Adds an email field

    class Meta:
        model = User  # tells django to use the built-in user model with the fields below
        fields = ['username', 'email', 'password']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
