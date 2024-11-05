from typing import Any
from django.contrib.auth.models import User
from django import forms
from .models import FoodType, Food
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class FoodForm(forms.ModelForm):
    
    class Meta:
        model = Food
        fields = ["nomi"]
        
    
class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "username"}
        )
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "password"}
        )
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "password again"}
        )
    )        

    remember_me = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"})
    )
    
    
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
            "remember_me",
        ]
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Username"}
            ),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Password"}
            ),
            "password2": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Password2"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ism"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Familiya"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
        }
        
 
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "username"}
        )
    )        
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "password"}
        )
    )
    
    
class CommentForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Izoh yozing"}
        ),
        max_length=1000,
    )