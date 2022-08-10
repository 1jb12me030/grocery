
from statistics import quantiles
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Registration(AbstractUser):
    username=models.CharField(max_length=40,unique=True)
    first_name=models.CharField(max_length=60, null=True, blank=True) 
    last_name=models.CharField(max_length=60, null=True, blank=True)
    email=models.CharField(max_length=60,unique=True,verbose_name='email',null=True, blank=True)
    
    location=models.TextField(null=True,blank=True)
    gender=models.CharField(max_length=6,null=True,blank=True)
    profile_pic=models.ImageField(upload_to='image',null=True,blank=True)
    mobile_no=models.CharField(max_length=13)
    birth_place=models.CharField(max_length=30,null=True,blank=True)
    
    occupation=models.CharField(max_length=40,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username + " " + self.email


class Category(models.Model):
    title = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural='categories'
    def __str__(self):
        return self.title
    
# class Grocery(models.Model):
#     user=models.ForeignKey(Registration,on_delete=models.CASCADE,)
#     title = models.CharField(max_length=150)
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)
#     brand = models.CharField(max_length=100, default='john doe')
#     isbn = models.CharField(max_length=13)
#     qualities = models.CharField(max_length=60)
#     price = models.IntegerField()
#     stock = models.IntegerField()
#     description = models.TextField()
#     imageUrl = models.ImageField(upload_to='image',null=True,blank=True)
#     # created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     status = models.BooleanField(default=True)
#     date_created = models.DateField(auto_now_add=True)
    
#     class Meta:
#         ordering = ['-date_created']
#     def __str__(self):
#         return self.title
    
    
    
    
class Product(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE,)
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageUrl = models.URLField()
    # created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']
    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)    
    
class Cart(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE,)
    # cart_id=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)    
    created_at=models.DateTimeField(auto_now_add=True)
    #grocery=models.ManyToManyField(Grocery)
    products=models.ManyToManyField(Product)
    
    # class Meta:
    #     ordering = ['cart_id', '-created_at']
        
    # def __str__(self):
    #     return f'{self.cart_id}'    
            
            
        

