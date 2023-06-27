from django.forms import ModelForm
from django import forms
from .models import Customer

class customerForm(ModelForm):
    name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Customer name'}))
    address=forms.CharField(max_length=500,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    house_no=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'House number'}))
    place=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'place'}))
    mobile=forms.CharField(max_length=12,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Contact number'}))
    mobile2=forms.CharField(max_length=12,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Contact number 2'}))
    pin_code=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Pin code'}))

    class Meta:
        model=Customer
        fields='__all__'
        exclude=['image','user']
        widget={
            'district':forms.Select(attrs={'class':'form-select','placeholder':'Select district','aria-label':"Default select example"}),
            'state':forms.Select(attrs={'class':'form-select','placeholder':'Select state','aria-label':"Default select example"})
        }