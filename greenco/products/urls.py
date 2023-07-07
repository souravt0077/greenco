from django.urls import path
from . import views

urlpatterns = [
    path('category/',views.category_page.as_view(),name='category'),
    # path('category_view/<str:slug>/',views.category_view.as_view(),name='category_view'),
    path('subcategory_view/<str:slug>/',views.subcategory_view.as_view(),name='subcategory_view'),
    path('products_view/<str:slug>/',views.products_view.as_view(),name='products_view'),
    path('product_details/<str:slug>/',views.product_details.as_view(),name='product_details'),
    # path('customer_details/',views.customer_details.as_view(),name='customer_details'),
    # path('remove_customer/<str:pk>/',views.remove_customer,name='remove_customer'),
    # path('update_customer/<str:pk>/',views.update_customer,name='update_customer'),
    # path('customer_address',views.customer_address,name='customer_address'),

    # add to cart
    path('add-to-cart/',views.addToCart,name='add-to-cart'),
    path('cart/',views.cart,name='cart'),
    path('remove_cart/<str:pk>/',views.remove_cart,name='remove_cart'),

    # update cart qty
    path('update_cart/',views.update_cart,name='update_cart'),

    # place order
    path('placeorder/',views.placeorder,name='placeorder'),




    # wishlist
    path('add_to_wishlist/',views.addtowishlist,name='add_to_wishlist'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('remove_wishlist/<str:pk>/',views.remove_wishlist,name='remove_wishlist'),

    # checkout
    path('checkout/',views.checkout,name='checkout'),

    path('smartphones/',views.smartphones,name='smartphones'),
    path('laptops/',views.laptops,name='laptops'),

    

]
