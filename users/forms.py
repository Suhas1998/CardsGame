from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
  first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
  last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
  email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

  class Meta:
      model = CustomUser
      fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image']
