from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^admin_login$',views.admin_login),
    url(r'^admin_dashboard$',views.admin_dashboard),
    url(r'^admin_index$',views.admin_index),
]
