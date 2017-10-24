from django.shortcuts import render, redirect

def index(request):
    context_dict = {}
    return render(request, 'restaurant/index.html', context_dict)
