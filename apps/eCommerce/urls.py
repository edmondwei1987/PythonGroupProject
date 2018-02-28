from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^admin_login$',views.admin_login),
    url(r'^admin_dashboard$',views.admin_dashboard),
    url(r'^admin_index$',views.admin_index),
    url(r'^admin/dashboard$',views.admin),
    url(r'^admin/index$',views.admin_index),
    url(r'^admin/products$',views.admin_products),
    url(r'^admin/orderdetail$',views.admin_orderdetail),
    url(r'^admin/productdetail$',views.admin_productdetail),
]
