from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from .forms import customerForm
from django.contrib import messages
from django.http import JsonResponse
import random

@method_decorator(login_required,name='dispatch')
class category_page(View):
    def get(self,request):
        category=MainCategory.objects.all()

        context={'category':category}
        return render(request,'categories.html',context)


@method_decorator(login_required,name='dispatch')
class subcategory_view(View):
    def get(self,request,slug):
        category=MainCategory.objects.all()
        categories=MainCategory.objects.filter(slug=slug)
        subcategory=SubCategory.objects.filter(category__slug=slug)
        subcategory_nos=len(categories)

        context={'subcategory':subcategory,'subcategory_nos':subcategory_nos,'category':category}
        return render(request,'subcategoryview.html',context)

@method_decorator(login_required,name='dispatch')
class products_view(View):
    def get(self,request,slug):
        category=MainCategory.objects.all()
        products=Product.objects.filter(category__slug=slug)
        cart_items=Cart.objects.filter(user=request.user)
        item_count=len(cart_items)
        wishlist_items=Wishlist.objects.filter(user=request.user)
        count=len(wishlist_items)
        context={'category':category,'products':products,'item_count':item_count,'count':count}
        return render(request,'products_view.html',context)

@method_decorator(login_required,name='dispatch')
class product_details(View):
    def get(self,request,slug):
        category=MainCategory.objects.all()
        products=Product.objects.filter(slug=slug)
        cart_items=Cart.objects.filter(user=request.user)
        item_count=len(cart_items)
        wishlist_items=Wishlist.objects.filter(user=request.user)
        count=len(wishlist_items)
        context={'products':products,'category':category,'item_count':item_count,'count':count}
        return render(request,'product_details.html',context)

@login_required(login_url='login')
def addToCart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            product_id=int(request.POST.get('id'))

            prod_ckeck = Product.objects.get(id=product_id)

            if prod_ckeck:
                item_in_cart=Cart.objects.filter(product_id=product_id,user=request.user)
                
                if item_in_cart :
                    
                    return JsonResponse({'status':'Product allready in cart'})
                else:
                    qty=int(request.POST.get('qty'))

                    Cart.objects.create(
                        product=prod_ckeck,
                        user=request.user,
                        product_qty=qty
                    )
                    return JsonResponse({'status':'Cart added successfully'})
            else:
                return JsonResponse({'status':'No product found'})
        else:
            return JsonResponse({'status':'Login to continue'})
    return redirect('home')


@login_required(login_url='login')
def cart(request):
    cart_items=Cart.objects.filter(user=request.user)
    category=MainCategory.objects.all()
    item_count=len(cart_items)
    wishlist_items=Wishlist.objects.filter(user=request.user)
    count=len(wishlist_items)
    amount=0
    for p in cart_items:
        value = p.product_qty * p.product.offer_price
        amount = amount + value
    if amount >= 2000:
        total_amount = amount
    else:
        total_amount= amount + 40

    context={'cart_items':cart_items,'item_count':item_count,'category':category,'count':count,'total_amount':total_amount,'amount':amount}
    return render(request,'cart.html',context)

def remove_cart(request,pk):
    cart_items=Cart.objects.filter(user=request.user,id=pk)
    cart_items.delete()
    return redirect('cart')

# update cart qty
@login_required(login_url='login')
def update_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('id'))
            if Cart.objects.filter(user=request.user,product_id=prod_id):
                prod_qty=int(request.POST.get('qty'))
                cart=Cart.objects.get(user=request.user,product_id=prod_id)
                cart.product_qty=prod_qty
                cart.save()
                return JsonResponse({'status':'Cart updated'})
        else:
            return JsonResponse({'status':'Login to continue'})
        
    return redirect('home')

# place order
@login_required(login_url='login')
def placeorder(request):
    if request.method == 'POST':
        current_user=User.objects.filter(id=request.user.id).first()

        if not current_user.first_name :
            current_user.first_name = request.POST.get('fname')
            current_user.last_name = request.POST.get('lname')
            current_user.save()
        
        if not Profile.objects.filter(user=request.user):
            userprofile=Profile()
            userprofile.user = request.user
            userprofile.fname = request.POST.get('fname')
            userprofile.fname = request.POST.get('lname')
            userprofile.email = request.POST.get('email')
            userprofile.city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.phone = request.POST.get('phone')
            userprofile.district = request.POST.get('district')
            userprofile.country = request.POST.get('country')
            userprofile.address = request.POST.get('address')
            userprofile.save()


        neworder=Order()
        neworder.user=request.user
        neworder.fname=request.POST.get('fname')
        neworder.email=request.POST.get('email')
        neworder.city=request.POST.get('city')
        neworder.state=request.POST.get('state')
        neworder.pincode=request.POST.get('pincode')
        neworder.lname=request.POST.get('lname')
        neworder.phone=request.POST.get('phone')
        neworder.district=request.POST.get('district')
        neworder.country=request.POST.get('country')
        neworder.message=request.POST.get('message')
        neworder.address=request.POST.get('address')
        neworder.payment_mode=request.POST.get('payment_mode')

        cart_items=Cart.objects.filter(user=request.user)

        amount=0
        for p in cart_items:
            value = p.product_qty * p.product.offer_price
            amount = amount + value
        if amount >= 2000:
            total_amount = amount
        else:
            total_amount= amount + 40
        
        neworder.total_price = total_amount

        trackno=request.user.username + str(random.randint(1111111,9999999))

        while Order.objects.filter(tracking_no=trackno) is None:
            trackno=request.user + str(random.randint(1111111,9999999))
        
        neworder.tracking_no = trackno
        neworder.save()

        for item in cart_items:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.offer_price,
                quantity=item.product_qty
            )
            # to reduce the quantity from available stock
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()

        # clear user cart
        Cart.objects.filter(user=request.user).delete()
        messages.success(request,'order has been placed successfully')
    return redirect('home')

def myorders(request):
    orders=Order.objects.filter(user=request.user)
    category=MainCategory.objects.all()
    context={'orders':orders,'category':category}
    return render(request,'orders/myorders.html',context)

def vieworder(request,t_no):
    orders=Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    order_items=OrderItem.objects.filter(order=orders)
    category=MainCategory.objects.all()

    context={'order_items':order_items,'orders':orders,'category':category}
    return render(request,'orders/vieworder.html',context)



# wishlist
@login_required(login_url='login')
def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id =request.POST.get('id')

            prod_check=Product.objects.get(id=prod_id)

            if prod_check:
                if Wishlist.objects.filter(user=request.user,product_id=prod_id):
                    return JsonResponse({'status':'All ready in wishlist'})
                else:
                    Wishlist.objects.create(
                        user=request.user,
                        product=prod_check
                    )
                    return JsonResponse({'status':'whishlist added'})
        else:
            return JsonResponse({'status':'User is not logged in'})
    else:
        return JsonResponse({'status':'Something wrong'})
    
    return redirect('home')

@login_required(login_url='login')
def wishlist(request):
    wishlist_items=Wishlist.objects.filter(user=request.user)
    count=len(wishlist_items)
    category=MainCategory.objects.all()
    cart_items=Cart.objects.filter(user=request.user)
    item_count=len(cart_items)
    context={'wishlist_items':wishlist_items,'count':count,'category':category,'item_count':item_count}
    return render(request,'wishlist.html',context)

@login_required(login_url='login')
def remove_wishlist(request,pk):
    wishlist_items=Wishlist.objects.filter(user=request.user,id=pk)
    wishlist_items.delete()
    messages.success(request,'deleted successfully')
    return redirect('wishlist')


# checkout
@login_required(login_url='login')
def checkout(request):
    cart_items=Cart.objects.filter(user=request.user)
    amount=0
    for p in cart_items:
        value = p.product_qty * p.product.offer_price
        amount = amount + value
    if amount >= 2000:
        total_amount = amount
    else:
        total_amount= amount + 40
    user_profile = Profile.objects.filter(user=request.user).first()
    wishlist_items=Wishlist.objects.filter(user=request.user)
    count=len(wishlist_items)
    cart_items=Cart.objects.filter(user=request.user)
    item_count=len(cart_items)
    category=MainCategory.objects.all()
    context={
        'cart_items':cart_items,
        'total_amount':total_amount,
        'user_profile':user_profile,
        'amount':amount,
        'count':count,
        'item_count':item_count,
        'category':category
        }
    return render(request,'checkout.html',context)


# Product based views
@login_required(login_url='login')
def smartphones(request):
    smartphone=MainCategory.objects.filter(name='Smartphone')
    context={'smartphone':smartphone}
    return render(request,'products/smartphones.html',context)

@login_required(login_url='login')
def laptops(request):
    laptop=MainCategory.objects.filter(name='Laptops')
    context={'laptop':laptop}
    return render(request,'products/laptops.html',context)



