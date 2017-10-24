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

    url(r'^add-food-item/$', views.add_food_item, name="add_food_item"),
    url(r'^edit-food-item/(?P<item_id>[0-9]+)$', views.edit_food_item, name="edit_food_item"),
    url(r'^delete-food-item/(?P<item_id>[0-9]+)$', views.delete_food_item, name="delete_food_item"),

]
