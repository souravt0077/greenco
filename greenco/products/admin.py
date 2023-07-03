from django.contrib import admin
from .models import MainCategory,Product,SubCategory,Customer,Cart,Wishlist

admin.site.register(MainCategory)
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Wishlist)