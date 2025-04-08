from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ModelForms(forms.ModelForm):
    class Meta:        
        model = models.Form
        fields = '__all__'
        labels={
            'name':'full name',
            'email':'email address',
            'phone':'enter phone number',            
            'course':'enter course',
        }
        help_texts={
            'name':'please enter your full name',            
            'course':'please enter your course'
        }        

class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']