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

    url(r'^restaurants/$', views.restaurant_list, name='restaurant_list'),
    url(r'^restaurants/(?P<restaurant_id>[0-9]+)$', views.restaurant_view, name='restaurant_view'),
    url(r'^restaurants/(?P<restaurant_id>[0-9]+)/(?P<food_item_id>[0-9]+)$', views.food_item_view, name='food_item_view'),

    url(r'^cart/$', views.cart_view, name='cart_view'),
    url(r'^cart/add/(?P<restaurant_id>[0-9]+)/(?P<food_item_id>[0-9]+)$', views.add_to_cart, name='add_to_cart'),
    url(r'^cart/clear$', views.cart_clear, name='cart_clear'),
    url(r'^checkout$', views.checkout, name='checkout'),
]
