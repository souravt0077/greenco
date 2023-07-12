from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import *
from django.db.models import Q


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

# search products
def search(request):
    category=MainCategory.objects.all()
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    products=Product.objects.filter(
        Q(name__icontains=q)
    )
    # available products count
    p_count=products.count()
    # cart items count
    cart_items=Cart.objects.filter(user=request.user)
    item_count=len(cart_items)
    wishlist_items=Wishlist.objects.filter(user=request.user)
    count=len(wishlist_items)
    context={'products':products,'q':q,'p_count':p_count,'category':category,'item_count':item_count,'count':count}
    return render(request,'search.html',context)
