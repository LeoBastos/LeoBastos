from django.http.response import HttpResponse
from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices,state_choices


def Index(request):
    listings = Listing.objects.all().order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }

    return render(request, 'pages/index.html', context)


def About(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp = Realtor.objects.all().filter(is_mvp=True)
    
    context = {
        'realtors': realtors,
        'mvp': mvp
    }
    return render(request, 'pages/about.html', context)


 