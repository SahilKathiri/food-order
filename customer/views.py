from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages

from carton.cart import Cart

from .models import Customer

from .forms import LoginForm

from restaurant.models import Restaurant, FoodItem


def customer_login(request):
    form = LoginForm()
    context_dict = {}
    context_dict['form'] = form
    return render(request, 'customer/login.html', context_dict)

def customer_auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('customer:index')
            else:
                return HttpResponse('Your account is disabled')
        else:
            print("Invalid login details: {0}, {1}.".format(username, password))
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request, 'customer/login.html', {})

def customer_logout(request):
    cart = Cart(request.session)
    cart.clear()
    logout(request)
    return redirect('customer:customer_login')

@login_required()
@permission_required('customer.view_customer_portal')
def index(request):
    username = request.user.username
    customer = Customer.objects.get(user__username=username)

    context_dict = {}
    context_dict['customer'] = customer
    return render(request, 'customer/index.html', context_dict)

@login_required()
@permission_required('customer.view_customer_portal')
def restaurant_list(request):
    restaurant_list = Restaurant.objects.all().order_by('user__username')
    context_dict = {}
    context_dict['restaurant_list'] = restaurant_list

    return render(request, 'customer/restaurant_list.html', context_dict)

@login_required()
@permission_required('customer.view_customer_portal')
def restaurant_view(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    food_items = FoodItem.objects.filter(restaurant=restaurant)

    context_dict = {}
    context_dict['restaurant'] = restaurant
    context_dict['food_items'] = food_items
    return render(request, 'customer/restaurant_view.html', context_dict)

@login_required()
@permission_required('customer.view_customer_portal')
def food_item_view(request, restaurant_id, food_item_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    food_item = FoodItem.objects.get(id=food_item_id)

    context_dict = {}
    context_dict['restaurant'] = restaurant
    context_dict['food_item'] = food_item
    return render(request, 'customer/food_item_view.html', context_dict)

@login_required()
@permission_required('customer.view_customer_portal')
def add_to_cart(request, restaurant_id, food_item_id):
    cart = Cart(request.session)
    food_item = FoodItem.objects.get(id=food_item_id)
    food_item.times_ordered += 1
    food_item.save()
    cart.add(food_item, price=food_item.price)
    messages.success(request, '{0} added to Cart'.format(food_item.name))
    return redirect('customer:restaurant_view', restaurant_id=restaurant_id)

@login_required()
@permission_required('customer.view_customer_portal')
def cart_view(request):
    return render(request, 'customer/cart_view.html', {})

@login_required()
@permission_required('customer.view_customer_portal')
def cart_clear(request):
    cart = Cart(request.session)
    cart.clear()
    messages.success(request, 'Cart Cleared')
    return redirect('customer:index')

@login_required()
@permission_required('customer.view_customer_portal')
def checkout(request):
    cart = Cart(request.session)
    messages.success(request, 'You have paid AED {0} for {1} item(s)'.format(cart.total, cart.count))
    messages.success(request, 'Thank you for shopping with us')
    cart.clear()
    return redirect('customer:index')
