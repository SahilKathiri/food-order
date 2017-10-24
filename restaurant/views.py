from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType

from .models import Restaurant, FoodItem

from .forms import LoginForm


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
    context_dict = {}
    return render(request, 'restaurant/index.html', context_dict)
