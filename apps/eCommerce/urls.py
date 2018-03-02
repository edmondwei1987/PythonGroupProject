from django.conf.urls import url
from . import views


urlpatterns=[

    url(r'^products/(?P<category_id>\d+)$', views.product),
    url(r'^products/show/(?P<product_id>\d+)$', views.product_detail),
    url(r'^buy/(?P<product_id>\d+)$', views.buy),
    url(r'^carts$', views.shopping_cart),
    url(r'^admin/index$',views.admin_index),
    url(r'^admin_login$',views.admin_login),
    # dashboard / order-display all
    url(r'^admin/dashboard$',views.admin_dashboard),

    url(r'^paymenttest$',views.paymenttest),
    url(r'^charge$',views.charge),
    url(r'^paymentresult/(?P<status>\w+)$',views.paymentresult),

    url(r'^admin/orderdetail/(?P<order_id>\d+)$',views.admin_orderdetail),
    # dashboard / product-display all
    url(r'^admin/products$',views.ProductListView.as_view()),

    # create new
    url(r'^admin/products/add$',views.admin_products_create_page),
    url(r'^admin/products/create$',views.admin_products_create),
    # edit product
    url(r'^admin/products/view/(?P<product_id>\d+)$',views.admin_productdetail),
    url(r'^admin/products/edit/(?P<product_id>\d+)$',views.admin_products_edit),
    url(r'^admin/products/delete/(?P<product_id>\d+)$',views.admin_products_delete),

]
