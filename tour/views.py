from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    tour = Tour.objects.all()
    return render(request, 'tour/home.html', context={"tours":tour})

def show_tour(request, tour_id):
    tour = Tour.objects.get(id=tour_id)
    return render(request, 'tour/tour_page.html', context={'tour':tour})
