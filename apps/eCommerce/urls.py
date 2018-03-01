from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^products$', views.product),
    url(r'^products/show/(?P<product_id>\d+)$', views.product_detail),
    url(r'^buy/(?P<item>\w+)$', views.buy),
    url(r'^carts$', views.shopping_cart),
    url(r'^admin/index$',views.admin_index),
    url(r'^admin_login$',views.admin_login),
    url(r'^admin/dashboard$',views.admin_dashboard),
    url(r'^admin/products$',views.admin_products),
    url(r'^admin/orderdetail$',views.admin_orderdetail),
    url(r'^admin/productdetail$',views.admin_productdetail),

]
