from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.core import validators

from .models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "field", "placeholder": "گذرواژه"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "field", "placeholder": "تکرار گذرواژه"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))

    class Meta:
        model = User
        fields = ('email', 'username')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("اختلافی در کلمه عبور وجود دارد")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_active', 'is_admin')


class LogInForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "email-input", "placeholder": "پست الکترونیک"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "password-input", "placeholder": "گذرواژه"}))