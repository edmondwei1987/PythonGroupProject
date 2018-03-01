# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

def admin_index(request):
    #login
    return render(request,'eCommerce/admin_index.html')

# username: admin
# password: python
def admin_login(request):
    # check if username in db
    try: 
        admin = Admin.objects.get(username = request.POST['username'])
    except:
        messages.error(request,'username or Password incorrect.')
        return redirect('/admin/index')
    # check if password correct
    if (request.POST['password'], admin.password):
        request.session['admin_id'] = admin.id
        return redirect('/admin/dashboard')
    else:
        messages.error(request,'Email or Password incorrect.')
        return redirect('/admin/index')

# ORDERS
def admin_dashboard(request):
    context = {
        'order' : Order.objects.all()
    }
    return render(request,'eCommerce/admin_orders.html', context)


def admin_orderdetail(request, order_id):
    this_order = Order.objects.get(id = order_id)
    context = {
        'order' : this_order,
        'order_detail' : Order_detail.objects.filter(order = this_order)
    }
    return render(request,'eCommerce/admin_orderdetail.html', context)


# ******************************PRODUCT***************************
#show all the products
def admin_products(request):
    products = Product.objects.all().order_by('id')
    context = {
        'product' : products
    }
    return render(request,'eCommerce/admin_products.html', context)
# Create new product
def admin_products_create_page(request):
    context = {
        'category' : Category.objects.all().order_by('name')
        }
    return render(request, 'eCommerce/admin_product_add.html', context)
def admin_products_create(request): 
    if len(request.POST['new_category']) > 0:
        category = Category.objects.create(name = request.POST['new_category'])
    else:
        category = Category.objects.get(id = request.POST['category'])
    Product.objects.create(category=category, name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    return redirect('/admin/products')
# Edit product details
def admin_productdetail(request, product_id):
    this_product = Product.objects.get(id = product_id)
    context = {
        'product' : this_product,
        'category' : Category.objects.all().order_by('name')
    }
    return render(request,'eCommerce/admin_productdetail.html', context)
def admin_products_edit(request, product_id):
    product = Product.objects.get(id = product_id)
    if len(request.POST['new_category']) > 0:
        category = Category.objects.create(name = request.POST['new_category'])
    else:
        category = Category.objects.get(id = request.POST['category'])
    product=Product(category=category, name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    product.save()
    return redirect('/admin/products')
# delete product
def admin_products_delete(request, product_id):
    Product.objects.get(id = product_id).delete()
    return redirect('/admin/products')
    
