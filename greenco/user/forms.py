from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm
from .models import User
from django import forms

class dateinput(forms.DateInput):
    input_type:str = 'date'

class greencoUserCreationForm(UserCreationForm):
    username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control my2 shadow','placeholder':'Username'}))
    email=forms.CharField(label='',max_length=200,widget=forms.EmailInput(attrs={'class':'form-control my2 shadow','placeholder':'email'}))
    dob=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control my-2 shadow','placeholder':'Year of birth'}))
    password1=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'class':'form-control my-2 shadow','placeholder':'Password'}))
    password2=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'class':'form-control my-2 shadow','placeholder':'Confirm Password'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2','dob']

        # widgets={
        #     'dob':dateinput()
        # }