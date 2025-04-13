from django.shortcuts import render

# Create your views here.

def login(request):
    context = {
        'title': 'Авторизация'
    }
    return render(request, '', context)

def registration(request):
    context = {
        'title': 'Регистрация'
    }
    return render(request, '', context)

def profile(request):
    context = {
        'title': ''
    }
    return render(request, 'Кабинет', context)

def logout(request):
    ...