
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('about',views.about,name='about'),
    path('listing',views.index,name='listing'),
    path('<int:listing_id>',views.listing,name='listing'),
    path('search',views.search,name='search'),
]