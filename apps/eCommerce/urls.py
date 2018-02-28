from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^admin/dashboard$',views.admin),
    url(r'^admin/index$',views.admin_index),
    url(r'^admin/products$',views.admin_products),
    url(r'^admin/orderdetail$',views.admin_orderdetail),
    url(r'^admin/productdetail$',views.admin_productdetail),
]
