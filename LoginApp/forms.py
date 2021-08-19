from django import forms
from django.db.models import fields
from django.forms import widgets
from . models import CustomUser

from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserForm(UserCreationForm):
    username=forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}))
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'address']
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'address':forms.Textarea(attrs={'class':'form-control','placeholder':'Address','cols':20,'rows':5}),
        }

class EditUserProfileForm(UserChangeForm):
    
    username=forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}))
    password = None
    class Meta:
        model = CustomUser
        fields=['username','email','address']
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'address':forms.Textarea(attrs={'class':'form-control','placeholder':'Address','cols':20,'rows':5}),
        }