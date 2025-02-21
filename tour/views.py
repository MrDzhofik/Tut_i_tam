from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
from .forms import ContactForm

# Create your views here.

def home(request):
    tour = Tour.objects.all()
    excursions = Excursion.objects.filter(public=True)
    context = {
        "tours": tour,
        "excursions": excursions
    }
    return render(request, 'tour/home.html', context)

def show_tour(request, tour_id):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name", "")
            form.save()
            form.email(name)
            return JsonResponse({"message": "Форма успешно отправлена!"})
        return JsonResponse({"errors": form.errors}, status=400)

    tour = Tour.objects.get(id=tour_id)
    program = Tour_Excursion.objects.filter(tour=tour)
    hotels = Tour_Hotel.objects.filter(tour=tour)
    context = {
                'form':form,
                'tour':tour, 
                'program': program,
                'hotels': hotels,
              }
    return render(request, 
                  'tour/tour_page.html', 
                  context=context)


def show_excursion(request, excursion_id):
    excursion = Excursion.objects.get(id=excursion_id)
    photos = Excursion_photo.objects.filter(excursion=excursion)
    context = {"excursion": excursion,
               "photos": photos,
              }
    
    return render(request, 'tour/excursion_page.html', context=context)

def show_hotel(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    photos = Hotel_photo.objects.filter(hotel=hotel)
    context = {
        "hotel": hotel,
        "photos": photos
    }
    return render(request, 'tour/hotel_page.html', context=context)


def excursion_order_show(request, excursion_id):
    excursion = Excursion.objects.get(id=excursion_id)
    photos = Excursion_photo.objects.filter(excursion=excursion)

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            form.email()
            return JsonResponse({"message": "Форма успешно отправлена!"})
        return JsonResponse({"errors": form.errors}, status=400)
    

    context = {
        "form":form,
        "excursion": excursion,
        "photos": photos,
              }
    
    return render(request, 'tour/excursion_order.html', context=context)
