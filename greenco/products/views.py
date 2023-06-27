from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import customerForm
from django.contrib import messages

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

        context={'category':category,'products':products}
        return render(request,'products_view.html',context)

@method_decorator(login_required,name='dispatch')
class product_details(View):
    def get(self,request,slug):
        category=MainCategory.objects.all()
        products=Product.objects.filter(slug=slug)
        context={'products':products,'category':category}
        return render(request,'product_details.html',context)

# customers details
@method_decorator(login_required,name='dispatch')
class customer_details(View):
    def get(self,request):
        form=customerForm()
        context={'form':form}
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

    context={'form':form}
    return render(request,'update_customer.html',context)

@login_required(login_url='login')
def customer_address(request):
    customers=Customer.objects.filter(user=request.user)
    context={'customers':customers}
    return render(request,'customer_address.html',context)



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

