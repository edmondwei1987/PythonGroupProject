from __future__ import unicode_literals

from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stripe_customer = models.CharField(max_length=255,default='')

class Address(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer_address')
    address = models.CharField(max_length = 255)
    address2 = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    zipcode = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Creditcard(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer_cc')
    address = models.ForeignKey(Address, related_name='address_cc')
    name_on_card = models.CharField(max_length = 255)
    # card_number = models.IntegerField()
    # sucurity_code = models.IntegerField()
    # exp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stripe_card = models.CharField(max_length=255,default='')

class Category(models.Model):
    name = models.CharField(max_length = 255)

class Product(models.Model):
    category =  models.ForeignKey(Category, related_name='category_product')
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer_ordered')
    address = models.ForeignKey(Address, related_name='address_ordered')
    credit_card = models.ForeignKey(Creditcard, related_name='creditcard_ordered')
    date = models.DateField()
    subtotal = models.FloatField()
    shipping = models.FloatField()
    status = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order_detail(models.Model):
    order = models.ForeignKey(Order, related_name='order_detail')
    product = models.ForeignKey(Product, related_name='product_detail')
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
