# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.views.generic import ListView

def product(request):
    # need function to go through page number
    # product_list = Product.objects.all()
    # paginator = Paginator(product_list, 15) # Show 15 contacts per page
    # page = request.GET.get('page')
    # products = Product.get_page(page)
    # if not 'price' in request.session:
    #     request.session['price'] = 0
    return render(request, 'customer/product.html') #not finish need to fingerout the logic

def product_detail(request, product_id):

    return render(request, 'customer/product_detail.html')
def buy(request, item):
    request.session['count'] = request.POST['quantity']
    product = Product.get(id = product_id)
    if item == product.name:
        price = product.price
        request.session['price'] = price
    return redirect('/carts')

def shopping_cart(request):
    product = Product.get(id = product_id)
    context = {
        'item': product.name,
        'price': product.price,
        'count': request.session['count'],
        'total': product.price *float(request.session['count'])
    }
    return render(request, 'customer/carts.html', context)
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

# ******************************ORDERS******************************
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
class ProductListView(ListView):
    model = Product
    template_name = "eCommerce/admin_products.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs) 
        list_product = Product.objects.all()
        paginator = Paginator(list_product, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            product_list = paginator.page(page)
        except PageNotAnInteger:
            product_list = paginator.page(1)
        except EmptyPage:
            product_list = paginator.page(paginator.num_pages)
        context['product'] = product_list
        return context

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
    
