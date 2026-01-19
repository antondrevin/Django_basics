from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from catalog.models import Product
from catalog.utils import greeting



# def home(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'home.html', context=context)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', "Пользователь")
#         return HttpResponse(f"{greeting()}, {name}! Мы получили Ваше сообщение")
#     return render(request, 'contacts.html')

class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


#
# def product_card(request, pk):
#     product = Product.objects.get(id=pk)
#     context = {'product': product}
#     return render(request, 'product_card.html', context=context)

class ProductCardDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_card.html'
    context_object_name = 'product'
