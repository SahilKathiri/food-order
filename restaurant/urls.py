from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'restaurant'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Authentication
    url(r'^login/$', views.restaurant_login, name='restaurant_login'),
    url(r'^auth/$', views.restaurant_auth, name='restaurant_auth'),
    url(r'^logout/$', views.restaurant_logout, name='restaurant_logout'),

]
