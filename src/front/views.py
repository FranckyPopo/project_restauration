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
    datas = {
        "sliders": SliderIndex.objects.all(),
        "menus": AddMenu.objects.all(),
        "list_avis": AvisClient.objects.all(),
        "solds": Sold.objects.all(),
        "background_image": BackgroundImageIndex.objects.first(),
        "about": AboutIndex.objects.first(),
        "contact_us": ContactUs.objects.first(),
        "link_reseau": LinkReseau.objects.first(),
    }
    return render(request, "front/pages/index.html", context=datas)

    
def fean_about(request):
    datas = {
        "about": AboutIndex.objects.first(),
        "background_image": BackgroundImageIndex.objects.first(),
    }
    return render(request, "front/pages/about.html", context=datas)
    
    
def fean_menu(request):
    datas = {
        "menus": AddMenu.objects.all(),
        "background_image": BackgroundImageIndex.objects.first(),
    }
    return render(request, "front/pages/menu.html", context=datas)
    
    
def fean_book(request):
    return render(request, "front/pages/book.html", context={"background_image": BackgroundImageIndex.objects.first()})
    
