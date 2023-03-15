from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request, name):
    print('index 함수 호출됨')
    print(f'name : {name}')

    apple = ['iphone', 'ipad', 'airpod', 'macbook',]

    context = {
        'name': name,
        'apple': random.sample(apple, 1),
    }

    print('index 함수 종료')
    return render(request, 'my_app/index.html', context)


# def login(request):
#     return render(request, 'login.html')
