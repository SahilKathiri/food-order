from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType

from .models import Customer

from .forms import LoginForm


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
    logout(request)
    return redirect('customer:customer_login')

@login_required()
@permission_required('customer.view_customer_portal')
def index(request):
    context_dict = {}
    return render(request, 'customer/index.html', context_dict)
