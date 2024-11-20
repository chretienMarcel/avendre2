from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import ProfileModel
from django.contrib.auth.forms import PasswordChangeForm


class signupform(UserCreationForm):
   
    username = forms.CharField(
        label=_("Username"),
        max_length=150,
    )
    email = forms.EmailField(
        label=_("Email"),
        max_length=150,
        help_text=_("Type your email address here:"),
    )
    first_name = forms.CharField(
        label=_("First Name"),
        max_length=30,
        required=True,
        help_text=_("Enter your first name."),
    )
    last_name = forms.CharField(
        label=_("Last Name"),
        max_length=30,
        required=True,
        help_text=_("Enter your last name."),
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=_("Your password must contain at least 8 characters."),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']  # Ajoutez ici les champs first_name et last_name
class userupdateform(forms.ModelForm):
        class Meta:
            model= User
            fields=['username','email']
class ProfileUpdateForm(forms.ModelForm):
        class Meta:
            model = ProfileModel
            fields= ['image'] 
class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
            

   