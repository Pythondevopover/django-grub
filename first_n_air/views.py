from django.shortcuts import redirect, render
from .models import Category, Sneakers, Advertising, Buy
from .forms import *
import random
import numpy as np
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
def home(request):
    ctg = Category.objects.all()
    advertising = Advertising.objects.all()
    sneaker = Sneakers.objects.all()
    random_sneak = random.choice(advertising)
    ctx = {
        'ctg': ctg,
        'sneaker': sneaker,
        'random_sneak': random_sneak
    }
    return render(request, "blog/index.html", ctx)

def contact(request):
    ctg = Category.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)  # Bu faqat debugging uchun, prod versiyada olib tashlanishi kerak
    ctx = {
        'ctg': ctg,
        'form': form  # Xatolarni ko'rsatish uchun formani kontekstga qo'shish kerak
    }
    return render(request, 'blog/contact.html', ctx)

def products(request, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    sneaker = Sneakers.objects.filter(type_id=category.id)
    ctx = {
        'ctg': ctg,
        'sneaker': sneaker,
        'category': category
    }
    return render(request, 'blog/products.html', ctx)

def register(request):
    """Handle user registration."""
    ctg = Category.objects.all()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form, 'ctg': ctg})
def login_view(request):
    """Handle user login."""
    ctg = Category.objects.all()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form, 'ctg': ctg})

def user_login(request):
    """Handle user login."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})

def single(request, pk=None):
    ctg = Category.objects.all()
    sneakers = Sneakers.objects.all()
    random_s = np.random.choice(sneakers, size=3, replace=False)
    products_pk = Sneakers.objects.get(pk=pk)
    form = ChoiceForm()
    if request.method == 'POST':
        form = ChoiceForm(request.POST, request.FILES)
        if form.is_valid():
            root = form.save()
            root = Buy.objects.get(pk=root.id)
            root.product = products_pk
            root.save()
            return redirect('home')
        else:
            print(form.errors)  # Bu faqat debugging uchun, prod versiyada olib tashlanishi kerak
    ctx = {
        'ctg': ctg,
        'products_pk': products_pk,
        'form': form,
        'random_s': random_s,
        'sneakers': sneakers
    }
    return render(request, 'blog/single.html', ctx)

@login_required
def user_logout(request):
    """Handle user logout."""
    logout(request)
    return redirect('home')

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
    authentication_form = AuthenticationForm
