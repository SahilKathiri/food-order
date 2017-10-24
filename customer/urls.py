from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'customer'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Authentication
    url(r'^login/$', views.customer_login, name='customer_login'),
    url(r'^auth/$', views.customer_auth, name='customer_auth'),
    url(r'^logout/$', views.customer_logout, name='customer_logout'),

]
