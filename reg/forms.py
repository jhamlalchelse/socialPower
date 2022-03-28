from enum import unique
from urllib import request
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import PostDetail

class UserRegistrationForms(UserCreationForm):
    username=forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    # mobilenum=forms.CharField(label='Mobile Number', widget=forms.NumberInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':True}))
    password = forms.CharField(label=_('Password'), strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password'}))
    class Meta:
        fields = ['username','mobilenum','password']

class UploadPostForm(forms.ModelForm):
    class Meta:
        model = PostDetail
        fields = ['post_image','desc']
        widgets = {'post_image': forms.FileInput(attrs={'class':'form-control'}), 'desc': forms.TextInput(attrs={'class':'form-control'})}