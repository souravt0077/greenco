from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required,name='dispatch')
class category_page(View):
    def get(self,request):
        category=MainCategory.objects.all()

        context={'category':category}
        return render(request,'categories.html',context)

# @method_decorator(login_required,name='dispatch')
# class category_view(View):
#     def get(self,request,slug):
#         category=MainCategory.objects.all()
#         categories=MainCategory.objects.filter(slug=slug)
#         category_nos=len(categories)

#         context={'categories':categories,'category_nos':category_nos,'category':category}
#         return render(request,'categoryview.html',context)

@method_decorator(login_required,name='dispatch')
class subcategory_view(View):
    def get(self,request,slug):
        category=MainCategory.objects.all()
        categories=MainCategory.objects.filter(slug=slug)
        subcategory=SubCategory.objects.filter(category__slug=slug)
        subcategory_nos=len(categories)

        context={'subcategory':subcategory,'subcategory_nos':subcategory_nos,'category':category}
        return render(request,'subcategoryview.html',context)

class products_view(View):
    def get(self,request,slug):
        category=MainCategory.objects.all()
        products=Product.objects.filter(category__slug=slug)

        context={'category':category,'products':products}
        return render(request,'products_view.html',context)
    
class product_details(View):
    def get(self,request,slug):
        category=MainCategory.objects.all()
        products=Product.objects.filter(slug=slug)
        context={'products':products,'category':category}
        return render(request,'product_details.html',context)




# Product based views

def smartphones(request):
    smartphone=MainCategory.objects.filter(name='Smartphone')
    context={'smartphone':smartphone}
    return render(request,'products/smartphones.html',context)

def laptops(request):
    laptop=MainCategory.objects.filter(name='Laptops')
    context={'laptop':laptop}
    return render(request,'products/laptops.html',context)