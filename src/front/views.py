from django.shortcuts import render
from .models import (
    SliderIndex, 
    AddMenu, 
    AboutIndex,
    BackgroundImageIndex, 
    AvisClient, 
    ContactUs,
    LinkReseau,
    
)

def fean_index(request):
    data = {
        "sliders": SliderIndex.objects.all(),
        "background_image": BackgroundImageIndex.objects.first(),
        "menus": AddMenu.objects.all(),
        "about": AboutIndex.objects.first(),
        "list_avis": AvisClient.objects.all(),
        "contact_us": ContactUs.objects.first(),
        "link_reseau": LinkReseau.objects.first(),
    }
    return render(request, "front/index.html", context=data)
    
def fean_about(request):
    return render(request, "front/about.html", context={"about": AboutIndex.objects.first()})
    
    
def fean_menu(request):
    menus = AddMenu.objects.all()
    return render(request, "front/menu.html", context={"menus": menus})
    
    
def fean_book(request):
    return render(request, "front/book.html")
    
