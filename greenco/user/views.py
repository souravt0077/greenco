from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import login,logout,authenticate
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import greencoUserCreationForm
from products.models import MainCategory
from datetime import date

class UserLogin(View):
    def get(self,request):
        page='login'
        context={'page':page}
        return render(request,'login_register.html',context)

    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user=User.objects.get(email=email)
        except:
            messages.error(request,'Email varification failed')
        
        user=authenticate(email=email,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'Welcome {}'.format(request.user))
            return redirect('home')
        else:
            messages.error(request,'No User Exist!')
            return redirect('login')
        

def userRegister(request):
    form=greencoUserCreationForm()
    if request.method == 'POST':
        form=greencoUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            this_year=date.today().year
            age=this_year - user.dob
            if user.dob < this_year:
                if age >= 18:

                    user.username = user.username.capitalize()
                    user.save()
                    login(request,user)
                    messages.success(request,'Successfully registerd Welcome {}'.format(request.user))
                    return redirect('home')
                else:
                    messages.error(request,'Sorry you are just {} year old child.Please see our guidlines'.format(age))
                    # return redirect('register')
            else:
                messages.error(request,'You enterd wrong year')
                # return redirect('register')

    context={'form':form}
    return render(request,'login_register.html',context)


@method_decorator(login_required,name='dispatch')
class UserLogout(View):
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request,'Logout successfully')
            return redirect('home')
        
@login_required(login_url='home')        
def userProfile(request):
    this_year=date.today().year
    age=this_year - request.user.dob  
    # customers=Customer.objects.filter(user=request.user)
    # address_count=len(customers)
    category=MainCategory.objects.all()
    context={'age':age,'category':category}
    return render(request,'profile.html',context)
        
def guidelines(request):
    return render(request,'guidelines.html')



