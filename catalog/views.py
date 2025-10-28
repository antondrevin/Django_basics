from django.http import HttpResponse
from django.shortcuts import render
from catalog.utils import greeting

def home(request):
    return render(request, 'home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f"{greeting()}, {name}! Мы получили Ваше сообщение")
    return render(request, 'contacts.html')
