from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
# Create your views here.


def index(request):
    category_list = Category.objects.all()
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['text'] = 'Hello world!'
    context_dict['categories'] = category_list
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')
