from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choice import price_choices, bedroom_choices, state_choices
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published =True)[:3]

    context = {'listings':listings,
               'price_choices': price_choices,
               'bedroom_choices': bedroom_choices,
               'state_choices': state_choices}
    return render(request, 'pages/index.html', context)

def about(request):
    #get all realtors

    realtors = Realtor.objects.all()
    #get mvp
    mvp = Realtor.objects.all().filter(is_mvp = True)
    context = {
        'realtors':realtors,
        'mvp':mvp
    }


    return render(request, 'pages/about.html',context)
     
