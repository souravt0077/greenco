from django.urls import path
from . import views

urlpatterns = [
    path('category/',views.category_page.as_view(),name='category'),
    # path('category_view/<str:slug>/',views.category_view.as_view(),name='category_view'),
    path('subcategory_view/<str:slug>/',views.subcategory_view.as_view(),name='subcategory_view'),
    path('products_view/<str:slug>/',views.products_view.as_view(),name='products_view'),
    path('product_details/<str:slug>/',views.product_details.as_view(),name='product_details'),


    path('smartphones/',views.smartphones,name='smartphones'),
    path('laptops/',views.laptops,name='laptops'),

    
]
