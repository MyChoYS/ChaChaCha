from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def test(request):
    return render(request, 'tt.html', None)

def index(request):
    return render(request, 'index.html', None)

def about(request) :
    return render(request, 'about.html', None)

def services(request) :
    return render(request, 'services.html', None)

def contact(request) :
    return render(request, 'contact.html', None)

def components(request) :
    return render(request, 'components.html', None)