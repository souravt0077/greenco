from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import *


@login_required(login_url='login')
def home(request):
    category=MainCategory.objects.all()
    offers=MainCategory.objects.filter(offer=True)
    cart_items=Cart.objects.filter(user=request.user)
    item_count=len(cart_items)
    wishlist_items=Wishlist.objects.filter(user=request.user)
    count=len(wishlist_items)
    context={'offers':offers,'category':category,'item_count':item_count,'count':count}

    return render(request,'home.html',context)

@login_required(login_url='login')
def about(request):
    context={}
    return render(request,'about.html',context)