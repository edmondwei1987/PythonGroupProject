# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
#at terminal enter 'pip install --upgrade stripe' to install stripe
import stripe

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

# Create your views here.
def admin_dashboard(request):
    #show all the orders on dashboard
    return render(request,'eCommerce/admin_orders.html')



def admin_products(request):
    #show all the products
    return render(request,'eCommerce/admin_products.html')

def admin_orderdetail(request):
    #show info of a single order
    return render(request,'eCommerce/admin_orderdetail.html')

def admin_productdetail(request):
    #update info for a product
    return render(request,'eCommerce/admin_productdetail.html')

def paymenttest(request):
    stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"

    creditcard=Creditcard.objects.get(id=1)
    cu = stripe.Customer.retrieve(creditcard.stripe_customer)
    card = cu.sources.retrieve(creditcard.stripe_card)

    return render(request,'eCommerce/payment_test.html',{'card':card})

def charge(request):
    stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"
    token=request.POST['stripeToken']
    srtipe_customer = stripe.Customer.create(
      # customer=request.session['id'],
      customer=1,
      source=token,
    )
    strip_card=srtipe_customer.sources.create(source=token)
    # charge = stripe.Charge.create(
    #   amount=999,
    #   currency="usd",
    #   description="Example charge",
    #   customer=srtipe_customer.id,
    #   source=token,
    # )


    # get customer from the session
    # customer=Customer.objects.get(id=request.session['id'])
    customer=Customer.objects.get(id=1)
    # create shipping address
    Address.objects.create(address=request.POST['address'],
    city=request.POST['city'],state=request.POST['state'],
    zipcode=request.POST['zipcode'],customer=customer)
    # create billing address
    billing_address=Address.objects.create(address=request.POST['baddress'],
    city=request.POST['bcity'],state=request.POST['bstate'],
    zipcode=request.POST['bzipcode'],customer=customer)
    # create credit card
    creditcard=Creditcard.objects.create(customer=customer,address=billing_address,stripe_card=srtipe_card.id,stripe_customer=stripe_customer.id,name_on_card=request.POST['bfullname'])


    return redirect('/paymentresult/'+charge.status)


def paymentresult(request,status):
    return render(request,'eCommerce/payment_result.html',{'status':status})
