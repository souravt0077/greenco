from django.contrib import admin
from .models import MainCategory,Product,SubCategory,Cart,Wishlist,Order,OrderItem,Profile

admin.site.register(MainCategory)
admin.site.register(Product)
admin.site.register(SubCategory)
# admin.site.register(Customer)

class cartAdmin(admin.ModelAdmin):
    list_display=['id','user','product']
admin.site.register(Cart,cartAdmin)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)