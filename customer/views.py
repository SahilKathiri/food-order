from django.shortcuts import render, redirect

def index(request):
    context_dict = {}
    return render(request, 'customer/index.html', context_dict)
