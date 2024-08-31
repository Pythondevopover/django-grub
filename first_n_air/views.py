from django.shortcuts import redirect, render
from .models import Category, Sneakers, Advertising, Buy
from .forms import ContactForm, RegisterForm, ChoiceForm
import random
import numpy as np

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
    ctg = Category.objects.all()
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    ctx = {'ctg': ctg, 'form': form}
    return render(request, 'blog/register.html', ctx)

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
