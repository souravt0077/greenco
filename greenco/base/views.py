from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    context={}
    return render(request,'home.html',context)

@login_required(login_url='login')
def about(request):
    context={}
    return render(request,'about.html',context)