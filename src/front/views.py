from django.shortcuts import render
from .models import (
    SliderIndex, 
    AddMenu, 
    AboutIndex,
    BackgroundImageIndex, 
    AvisClient, 
    ContactUs,
    LinkReseau,
    Sold,
    
)

def fean_index(request):
    data = {
        "sliders": SliderIndex.objects.all(),
        "menus": AddMenu.objects.all(),
        "list_avis": AvisClient.objects.all(),
        "solds": Sold.objects.all(),
        "background_image": BackgroundImageIndex.objects.first(),
        "about": AboutIndex.objects.first(),
        "contact_us": ContactUs.objects.first(),
        "link_reseau": LinkReseau.objects.first(),
    }
    return render(request, "front/pages/index.html", context=data)
   
    
def fean_about(request):
    return render(request, "front/pages/about.html", context={"about": AboutIndex.objects.first()})
    
    
def fean_menu(request):
    return render(request, "front/pages/menu.html", context={"menus": AddMenu.objects.all()})
    
    
def fean_book(request):
    return render(request, "front/pages/book.html")
    
