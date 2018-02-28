# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def admin(request):
    return render(request,'eCommerce/admin_orders.html')

def admin_index(request):
    return render(request,'eCommerce/admin_index.html')
