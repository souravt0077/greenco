from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import customerForm
from django.contrib import messages
from django.http import JsonResponse

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

# customers details
@method_decorator(login_required,name='dispatch')
class customer_details(View):
    def get(self,request):
        form=customerForm()
        cart_items=Cart.objects.filter(user=request.user)
        item_count=len(cart_items)
        context={'form':form,'item_count':item_count}
        return render(request,'customer.html',context)
    
    def post(self,request):
        form=customerForm(request.POST)
        if form.is_valid():
            customer=form.save(commit=False)
            customer.user=request.user
            customer.save()
            messages.success(request,'Address added successfully')
            return redirect('profile')
        else:
            messages.error(request,'Address not added')
        
        context={'form':form}
        return render(request,'customer.html',context)
    
@login_required(login_url='login')
def remove_customer(request,pk):
    customer_add=Customer.objects.get(id=pk)
    customer_add.delete()
    messages.success(request,'Address removed ')
    return redirect('profile')

@login_required(login_url='login')
def update_customer(request,pk):
    customer_add=Customer.objects.get(id=pk)
    
    form=customerForm(instance=customer_add)
    if request.method == 'POST':
        form=customerForm(request.POST, instance=customer_add)
        if form.is_valid():
            customer=form.save(commit=False)
            customer.user=request.user
            customer.save()
            messages.success(request,'Updated successfully')
            return redirect('profile')
        else:
            messages.error(request,'Update failed')
    cart_items=Cart.objects.filter(user=request.user)
    item_count=len(cart_items)
    context={'form':form,'item_count':item_count}
    return render(request,'update_customer.html',context)

@login_required(login_url='login')
def customer_address(request):
    cart_items=Cart.objects.filter(user=request.user)
    item_count=len(cart_items)
    customers=Customer.objects.filter(user=request.user)
    context={'customers':customers,'item_count':item_count}
    return render(request,'customer_address.html',context)


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



def cart(request):
    cart_items=Cart.objects.filter(user=request.user)
    category=MainCategory.objects.all()
    item_count=len(cart_items)
    wishlist_items=Wishlist.objects.filter(user=request.user)
    count=len(wishlist_items)


    context={'cart_items':cart_items,'item_count':item_count,'category':category,'count':count}
    return render(request,'cart.html',context)

def remove_cart(request,pk):
    cart_items=Cart.objects.filter(user=request.user,id=pk)
    cart_items.delete()
    return redirect('cart')

# wishlist

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

def wishlist(request):
    wishlist_items=Wishlist.objects.filter(user=request.user)
    count=len(wishlist_items)
    category=MainCategory.objects.all()
    cart_items=Cart.objects.filter(user=request.user)
    item_count=len(cart_items)
    context={'wishlist_items':wishlist_items,'count':count,'category':category,'item_count':item_count}
    return render(request,'wishlist.html',context)

def remove_wishlist(request,pk):
    wishlist_items=Wishlist.objects.filter(user=request.user,id=pk)
    wishlist_items.delete()
    messages.success(request,'deleted successfully')
    return redirect('wishlist')





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



