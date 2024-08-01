from django.shortcuts import render
from .models import Special,Services,Trainers,Price,Questions


def home(requests):
    Specials = Special.objects.filter(statue = True)
    context = {
        'specials':Specials
    }
    return render(requests,'root/index.html',context=context)

def about(requests):
    return render(requests,'root/index.html')

def features(requests):
    return render(requests,'root/index.html')

def services(requests):
    service = Services.objects.filter(statue = True)
    context = {
        'service':service
    }
    return render(requests,'root/index.html',context=context)

def pricing(requests):
    prices = Price.objects.filter(statue = True)
    context = {
        'prices':prices
    }
    return render(requests,'root/index.html',context=context)

def contact(requests):
    return render(requests,'root/index.html')
