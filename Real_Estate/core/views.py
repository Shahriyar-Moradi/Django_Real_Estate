
from django.shortcuts import render
from django.http import HttpResponse
from property_listing.models import Listing
from realtor.models import Realtor
from property_listing.choices import price_choices,bedroom_choices,state_choices
from django.shortcuts import render, get_object_or_404
from property_listing.models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from property_listing.choices import price_choices, bedroom_choices, state_choices




def search(request):
    queryset_list = Listing.objects.order_by('list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if keywords:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if keywords:
            queryset_list = queryset_list.filter(city__iexact=state)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)





# Create your views here.
def home(request):
    listings=Listing.objects.order_by('list_date').filter(is_published=True)[:3]
    context={
        'listings':listings,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices,
    }
    return render(request,'pages/index.html',context)

def about(request):
    realtors=Realtor.objects.order_by('hire_date')
    mvp_realtors=Realtor.objects.all().filter(is_mvp=True)
    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }
    return render(request,'pages/about.html',context)