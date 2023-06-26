from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import *

@login_required(login_url='login')
def home(request):
    category=MainCategory.objects.all()
    offers=MainCategory.objects.filter(offer=True)
    context={'offers':offers,'category':category}
    return render(request,'home.html',context)

@login_required(login_url='login')
def about(request):
    context={}
    return render(request,'about.html',context)