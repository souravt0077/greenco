from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import MyPasswordChangeForm
urlpatterns = [
    path('login/',views.UserLogin.as_view(),name='login'),
    path('register/',views.userRegister,name='register'),
    path('logout/',views.UserLogout.as_view(),name='logout'),

    # Guideline
    path('guidelines/',views.guidelines,name='guidelines'),

    # change password
    path('changepassword/',auth_view.PasswordChangeView.as_view(template_name='changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='changepassword'),
    # password change done 
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html',),name='passwordchangedone')
]
