from django.shortcuts import render
from .models import SliderIndex, AddMenu, AboutIndex, BackgroundImageIndex

def fean_index(request):

    data = {
        "sliders": SliderIndex.objects.all(),
        "background_image": BackgroundImageIndex.objects.first(),
        "menus": AddMenu.objects.all(),
        "about": AboutIndex.objects.first(),
        
    }
    return render(request, "front/index.html", context=data)
    
def fean_about(request):
    return render(request, "front/about.html")
    
    
def fean_menu(request):
    return render(request, "front/menu.html")
    
    
def fean_book(request):
    return render(request, "front/book.html")
    
    
