# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
#at terminal enter 'pip install --upgrade stripe' to install stripe
import stripe
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.views.generic import ListView


def product(request, category_id):
    if category_id  == '0':
        product = Product.objects.all(),
    else:
    # need function to go through page number

        category = Category.objects.get(id = category_id)
        product = Product.objects.filter(category = category)
    context = {
            "product_list": product,
            "category": Category.objects.all()
    }
    return render(request, 'customer/product.html', context) #not finish need to fingerout the logic


def product_detail(request, product_id):
    context = {
        "product":Product.objects.get(id = product_id)
    }
    return render(request, 'customer/product_detail.html', context)




def buy(request, product_id):
    if not 'cart' in request.session:
        request.session['cart'] = []

    products_buy = {
        'product_id': product_id,
        'quantity': request.POST['quantity']
    }
    request.session['cart'].append(products_buy)
    print request.session['cart']
    request.session.modified = True
    return redirect('/carts')

def shopping_cart(request):
    products = []
    for each in  request.session['cart']:
        print each
        banana ={
            'apple':Product.objects.get(id = each['product_id']),
            'quantity': each['quantity'],
        }
        products.append(banana)
    context = {
        'products': products
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



def paymenttest(request):
    stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"

    customer=Customer.objects.get(id=1)
    # for cus in Customer.objects.all():
    #     print str(cus.id)+":"+cus.stripe_customer
    stripe_cards= stripe.Customer.retrieve(customer.stripe_customer).sources.all(object="card")

    return render(request,'eCommerce/payment_test.html',{'cards':stripe_cards})

def charge(request):
    stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"
    token=request.POST['stripeToken']

    # customer = Customer.objects.get(id=request.session['id'])
    customer = Customer.objects.get(id=1)
    stripe_customer = stripe.Customer.retrieve(customer.stripe_customer)
    stripe_card=stripe_customer.sources.create(source=token)
    stripe_card_id=stripe_card.id


    # create shipping address
    Address.objects.create(address=request.POST['address'],
    city=request.POST['city'],state=request.POST['state'],
    zipcode=request.POST['zipcode'],customer=customer)
    # create billing address
    billing_address=Address.objects.create(address=request.POST['baddress'],
    city=request.POST['bcity'],state=request.POST['bstate'],
    zipcode=request.POST['bzipcode'],customer=customer)
    # create credit card
    creditcard=Creditcard.objects.create(customer=customer,address=billing_address,stripe_card=stripe_card_id,name_on_card=request.POST['bfullname'])
    # charge the card
    charge = stripe.Charge.create(
      amount=999,
      currency="usd",
      description="Example charge",
      customer=stripe_customer.id,
    )

    return redirect('/paymentresult/'+charge.status)


def add_default_card(request):
    # customer=Customer.objects.get(id=request.session['id'])
    customer=Customer.objects.get(id=1)
    stripe_customer = stripe.Customer.create(
    # customer=request.session['id'],
    customer=1,
    source=token,
    )
    customer.stripe_customer=stripe_customer.id
    customer.save()
    stripe_card_id=''

    # create shipping address
    Address.objects.create(address=request.POST['address'],
    city=request.POST['city'],state=request.POST['state'],
    zipcode=request.POST['zipcode'],customer=customer)
    # create billing address
    billing_address=Address.objects.create(address=request.POST['baddress'],
    city=request.POST['bcity'],state=request.POST['bstate'],
    zipcode=request.POST['bzipcode'],customer=customer)
    # create credit card
    creditcard=Creditcard.objects.create(customer=customer,address=billing_address,stripe_card=stripe_card_id,name_on_card=request.POST['bfullname'])
    # charge the card
    charge = stripe.Charge.create(
      amount=999,
      currency="usd",
      description="Example charge",
      customer=stripe_customer.id,
    )

def paymentresult(request,status):
    return render(request,'eCommerce/payment_result.html',{'status':status})
