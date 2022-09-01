from cProfile import label
from dataclasses import field, fields
from tkinter.ttk import LabeledScale
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Blog


class SignupForm(UserCreationForm):
    # password2= forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
        labels ={'email':'Email'}



class BlogForms(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['Title','Description','Image','Author']
        # widgets={"date":forms.DateTimeInput(format="%Y-%m-%d %H:%M:%S")}