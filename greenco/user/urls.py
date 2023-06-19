from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.UserLogin.as_view(),name='login'),
    path('register/',views.userRegister,name='register'),
    path('logout/',views.UserLogout.as_view(),name='logout'),

    # Guideline
    path('guidelines/',views.guidelines,name='guidelines'),
]
