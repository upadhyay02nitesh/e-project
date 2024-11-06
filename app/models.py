from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator

STATE_CHOICES=(
    ('Andaman & Nicobar Islands','Andman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunchal Pradesh', 'Arunchal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chadighar','Chadighar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Gujrat','Gujrat'),
    ('Harayan','Harayan'),
    ('Himanchal Pradesh','Himanchal Pradesh'),
    ('Jammu & Kasmir','Jammu & Kasmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerla','Kerla'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Goa','Goa'),
    ('uttar Pradesh','uttar Pradesh'),
    ('West Bengal','West Bengal'),
    ('Uttrakhand','Uttrakhand'),
    ('Tripura','Tripura'),
    ('Telangana','Telangana'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Odisha','Odisha'),
    ('Rajasthan','Rajasthan'),
    ('Mizoram','Mizoram'),



)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200,null=True)
    locality = models.CharField(max_length=200,default="Unknown")
    city = models.CharField(max_length=50 ,default="Unknown")
    # zipcode = models.CharField(max_length=10,default='00000')
    zipcode = models.IntegerField(null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=50,default="Unknown")

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),

)



class Category(models.Model):
    name = models.CharField(max_length=255 ,default='default_category',null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=100,null=True)
    selling_price = models.FloatField(null=True)
    discounted_price = models.FloatField(null=True)
    description = models.TextField(null=True)
    brand = models.CharField(max_length=100,null=True)                               #default='default_category'
    catagory = models.CharField(choices=CATEGORY_CHOICES,max_length=2,null=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=2,null=True )
    # category = models.ForeignKey(category, related_name='products', on_delete=models.CASCADE,default=1)
    product_image = models.ImageField(upload_to='productimg',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)


    def __str__(self):
        return str(self.id)

# ///////////////////

# class Category(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,max_length=2)
#     image = models.ImageField(upload_to='products/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

class Cart(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1,null=True)
    name = models.CharField(max_length=255 ,  default='default_name',null=True)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')

)

class OrderPlaced(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1,null=True)
    ordered_date = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending',null=True)
    name = models.CharField(max_length=255 , default='default_name',null=True)


    def __str__(self):
         return str(self.id)
         
    @property
    def total_cost(self):
        # return self.quantity * self.product.discounted_price
        return self.quantity * (self.product.discounted_price or 0)
    

    

    

# Create your models here.
