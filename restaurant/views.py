from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.contrib import messages

from .models import Restaurant, FoodItem

from .forms import LoginForm, FoodItemForm, RestaurantProfileForm


def restaurant_login(request):
    form = LoginForm()
    context_dict = {}
    context_dict['form'] = form
    return render(request, 'restaurant/login.html', context_dict)

def restaurant_auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('restaurant:index')
            else:
                return HttpResponse('Your account is disabled')
        else:
            print("Invalid login details: {0}, {1}.".format(username, password))
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request, 'restaurant/login.html', {})

def restaurant_logout(request):
    logout(request)
    return redirect('restaurant:restaurant_login')

@login_required()
@permission_required('restaurant.view_restaurant_portal')
def index(request):
    username = request.user.username
    restaurant = Restaurant.objects.get(user__username=username)
    restaurant_name = "{0} {1}".format(restaurant.user.first_name, restaurant.user.last_name)
    food_items = FoodItem.objects.filter(restaurant=restaurant)

    context_dict = {}
    context_dict['restaurant_name'] = restaurant_name
    context_dict['food_items'] = food_items
    return render(request, 'restaurant/index.html', context_dict)

@login_required()
@permission_required('restaurant.view_restaurant_portal')
def edit_profile(request):
    username = request.user.username
    instance = Restaurant.objects.get(user__username=username)
    if request.method == "POST":
        form = RestaurantProfileForm(request.POST, instance=instance)
        if form.is_valid():
            instance.phone_no = form.cleaned_data['phone_no']
            instance.address_1 = form.cleaned_data['address_1']
            instance.address_2 = form.cleaned_data['address_2']
            instance.address_emirate = form.cleaned_data['address_emirate']
            instance.save()
            messages.success(request, 'Profile Edited')
            return redirect('restaurant:index')
    else:
        form = RestaurantProfileForm(initial=model_to_dict(instance))

    context_dict = {}
    context_dict['initial'] = instance
    context_dict['form'] = form
    return render(request, 'restaurant/profile.html', context_dict)

@login_required()
@permission_required('restaurant.view_restaurant_portal')
def add_food_item(request):
    username = request.user.username
    restaurant = Restaurant.objects.get(user__username=username)
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            food_item = FoodItem.objects.create(name=name,
                            price=price,
                            description=description,
                            restaurant=restaurant,
                            times_ordered=0)
            messages.success(request, 'Food Item Added: %s' % name)
            return redirect('restaurant:index')
    else:
        form = FoodItemForm()

    context_dict = {}
    context_dict['form'] = form
    return render(request, 'restaurant/add_food_item.html', context_dict)

@login_required()
@permission_required('restaurant.view_restaurant_portal')
def edit_food_item(request, item_id):
    instance = FoodItem.objects.get(id=item_id)
    if request.method == "POST":
        form = FoodItemForm(request.POST, instance=instance)
        if form.is_valid():
            instance.name = form.cleaned_data['name']
            instance.price = form.cleaned_data['price']
            instance.description = form.cleaned_data['description']
            instance.save()
            messages.success(request, 'Food Item Edited: %s' % instance.name)
            return redirect('restaurant:index')
    else:
        form = FoodItemForm(initial=model_to_dict(instance))

    context_dict = {}
    context_dict['initial'] = instance
    context_dict['form'] = form
    context_dict['deletable'] = True
    return render(request, 'restaurant/add_food_item.html', context_dict)

@login_required()
@permission_required('restaurant.view_restaurant_portal')
def delete_food_item(request, item_id):
    food_item = FoodItem.objects.get(id=item_id)
    msg_arg = food_item.name
    food_item.delete()

    messages.success(request, 'Food Item Deleted: %s' % msg_arg)
    return redirect('restaurant:index')
