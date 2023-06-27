from django.contrib import admin
from .models import MainCategory,Product,SubCategory,Customer

admin.site.register(MainCategory)
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Customer)