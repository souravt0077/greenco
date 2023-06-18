from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import login,logout,authenticate
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import greencoUserCreationForm

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

            user.username = user.username.capitalize()
            user.save()
            login(request,user)
            messages.success(request,'Successfully registerd Welcome {}'.format(request.user))
            return redirect('home')
        else:
            messages.error(request,'Something went wrong')
            return redirect('register')

    context={'form':form}
    return render(request,'login_register.html',context)


@method_decorator(login_required,name='dispatch')
class UserLogout(View):
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request,'Logout successfully')
            return redirect('home')
        




