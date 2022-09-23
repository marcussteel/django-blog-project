#user creation formu django dan çekeceğiz ekstaradan email formunu alacağız.

from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
#email ve first name forma ekleme

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "first_name")
    #email filedı unique olmalı, herkes ayı epostayı girmemeli valifda00000000ti0on yapmalıyız
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('please use another mail')
        return email

    def clean_first_name(self):
        name = self.cleaned_data['first_name']
        if "a" in name:
            raise forms.ValidationError("gözünün üstünde kaşın var . bir de  a var")

#iki formu tek sayfada gösterme
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("image", "bio")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")
