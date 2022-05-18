from django.contrib import admin
from .models import *

models = [
    SliderIndex, 
    BackgroundImageIndex, 
    AboutIndex, 
    BookTable, 
    AvisClient, 
    ContactUs, 
    LinkReseau, 
    Sold,
    AddMenu, 
]

for model in models: admin.site.register(model)


