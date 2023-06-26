from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm


urlpatterns = [
    path('login/',views.UserLogin.as_view(),name='login'),
    path('register/',views.userRegister,name='register'),
    path('logout/',views.UserLogout.as_view(),name='logout'),

    # Guideline
    path('guidelines/',views.guidelines,name='guidelines'),

    # change password
    path('changepassword/',auth_view.PasswordChangeView.as_view(template_name='changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='changepassword'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),

    # Reset Password
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='reset_password/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password_reset_done/',auth_view.PasswordResetDoneView.as_view(template_name='reset_password/password_reset_done.html',),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='reset_password/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password_reset_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='reset_password/password_reset_complete.html'),name='password_reset_complete'),

]
