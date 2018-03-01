# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def product(request):
    return render(request, 'customer/product.html')
