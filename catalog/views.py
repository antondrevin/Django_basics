from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product
from catalog.utils import greeting

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context=context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name', "Пользователь")
        return HttpResponse(f"{greeting()}, {name}! Мы получили Ваше сообщение")
    return render(request, 'contacts.html')

def product_card(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'product_card.html', context=context)
