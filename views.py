from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

posts = [
    {
        'author': 'Mr R L',
        'title': 'Prouct review - drinks',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Miss J D',
        'title': 'Service feedback',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    return render(request, 'tredegars/home.html',  {'title': 'SJT Wholesale'})

def products(request):
    return render(request, 'tredegars/products.html', {'title': 'Products'})

def about(request):
    context = {
        'posts': posts,
        'title': 'About'
    }
    return render(request, 'tredegars/about.html',context)

def contact(request):
    return render(request, 'tredegars/contact.html', {'title': 'Contact'})

def register(request):
    form = UserCreationForm(request.POST)
    return render(request, 'tredegars/register.html', {'form': form, 'title': 'User registration'})