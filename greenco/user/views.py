from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import login,logout,authenticate
from .models import User
from django.contrib import messages
# Create your views here.

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
            messages.error(request,'Something Went wrong!')
            return redirect('login')
        


class UserRegister(View):
    def get(self,request):
        context={}
        return render(request,'login_register.html',context)

    def post(self,request):
        pass

class UserLogout(View):
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request,'Logout successfully')
            return redirect('home')