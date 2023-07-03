from django.db import models
from user.models import User 

DISTRICT_CHOICES=(
    ('kasrgod','kasrgod'),
    ('Kannur','Kannur'),
    ('Wayanad','Wayanad'),
    ('Kozhikode','Kozhikode'),
    ('Malappuram','Malappuram'),
    ('Palakkad','Palakkad'),
    ('Thrissur','Thrissur'),
    ('Ernakulam','Ernakulam'),
    ('Idukki','Idukki'),
    ('Kottayam','Kottayam'),
    ('Alappuzha','Alappuzha'),
    ('Pathanamthitta','Pathanamthitta'),
    ('Kollam','Kollam'),
    ('Thiruvanathapuram','Thiruvanathapuram'),

)

STATE_CHOICES=(
    ('Andaman & nicobar islands','Andaman & nicobar islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chattisgarh','Chattisgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman and diu','Daman and diu'),
    ('Delhi','Delhi'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Hariyana','Hariyana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu & kashmir','Jammu & kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshdweep','Lakshdweep'),
    ('Madhya dPradesh','Madhya dPradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Missoram','Missoram'),
    ('Nagaland','Nagaland'),
    ('Odisa','Odisa'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamilnadu','Tamilnadu'),
    ('Telengana','Telengana'),
    ('Tripura','Tripura'),
    ('Utharakhand','Utharakhand'),
    ('Utter pradesh','Utter pradesh'),
    ('West bengal','West bengal'),
)




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
    quantity=models.IntegerField(default=1)
    about=models.TextField(max_length=250)
    features=models.TextField(max_length=500,null=True,blank=True)
    offer=models.BooleanField(default=False)
    added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='customer',null=True)
    address=models.TextField(max_length=500)
    house_no=models.IntegerField(null=True)
    place=models.CharField(max_length=150,null=True)
    district=models.CharField(choices=DISTRICT_CHOICES ,max_length=150,null=True)
    state=models.CharField(choices=STATE_CHOICES,max_length=150,null=True)
    mobile=models.CharField(max_length=12)
    mobile2=models.CharField(max_length=12)
    pin_code=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['-created_at']

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.user,self.product)

    class Meta:
        ordering=['-created_at']

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.user,self.product)

    class Meta:
        ordering=['-created_at']