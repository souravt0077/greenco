from django.db import models
from user.models import User 
# Create your models here.

class MainCategory(models.Model):
    slug=models.SlugField()
    name=models.CharField(max_length=200,unique=True)
    category_image=models.ImageField(upload_to='category_images')
    about=models.TextField(max_length=250)
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    slug=models.SlugField()
    category=models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,unique=True)
    category_image=models.ImageField(upload_to='subcategory_images')
    about=models.TextField(max_length=250)
    offer=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Product(models.Model):
    slug=models.SlugField()
    name=models.CharField(max_length=200,unique=True)
    category=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    product_images1=models.ImageField(upload_to='product_images',null=True,blank=True)
    product_images2=models.ImageField(upload_to='product_images',null=True,blank=True)
    product_images3=models.ImageField(upload_to='product_images',null=True,blank=True)
    product_images4=models.ImageField(upload_to='product_images',null=True,blank=True)
    product_images5=models.ImageField(upload_to='product_images',null=True,blank=True)
    selling_price=models.IntegerField(default=0)
    offer_price=models.IntegerField(default=0)
    about=models.TextField(max_length=250)
    features=models.TextField(max_length=500,null=True,blank=True)
    offer=models.BooleanField(default=False)
    added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


