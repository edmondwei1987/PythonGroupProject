from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^admin/dashboard$',views.admin_dashboard),
    url(r'^admin/index$',views.admin_index),
    url(r'^admin_login$',views.admin_login),
    url(r'^admin/dashboard$',views.admin_dashboard),
    url(r'^admin/products$',views.admin_products),
    url(r'^admin/orderdetail$',views.admin_orderdetail),
    url(r'^admin/productdetail$',views.admin_productdetail),
    url(r'^paymenttest$',views.paymenttest),
    url(r'^charge$',views.charge),
    url(r'^paymentresult/(?P<status>\w+)$',views.paymentresult),

]
