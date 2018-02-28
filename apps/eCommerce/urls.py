from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^admin/dashboard$',views.admin),
    url(r'^admin/index$',views.admin_index),
]
