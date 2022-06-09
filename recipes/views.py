from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')


def contact(request):
    return HttpResponse('Pagina Contato')


def about(request):
    return HttpResponse('Pagina Sobre')
