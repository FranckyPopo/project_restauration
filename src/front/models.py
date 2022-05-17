from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class SliderIndex(models.Model):
    title = models.CharField(max_length=125)
    description = models.CharField(max_length=250)
    date_create = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.title
    
class BackgroundImageIndex(models.Model):
    # Cette class va me permetre de changer l'image de font de la page d'acceuil
    background_image = models.ImageField()
    date_create = models.DateTimeField(default=timezone.now())

class AddMenu(models.Model):
    foods = [
        ("burger", "burger"),
        ("pizza", "pizza"),
        ("pasta", "pasta"),
        ("fries", "fries"),
    ]
    
    menu_image = models.ImageField()
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=150)
    type_food = models.CharField(choices=foods, max_length=10, default="Burger")
    date_create = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.title

class AboutIndex(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=205)
    image_about = models.ImageField()
    date_create = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.title

class BookTable(models.Model):
    name = models.CharField(max_length=150)
    number_phone = PhoneNumberField()
    email = models.EmailField(max_length=150)
    number_person = models.IntegerField(validators=[MaxValueValidator(1), MinValueValidator(999)])
    date_create = models.DateTimeField(default=timezone.now())

class AvisClient(models.Model):    
    photo_client = models.ImageField()
    name_client = models.CharField(max_length=150)
    message = models.CharField(max_length=250)
    date_create = models.DateTimeField(default=timezone.now())
    
    def __str__(self) -> str:
        return self.name_client
    
class ContactUs(models.Model):
    location = models.URLField()
    number_phone = PhoneNumberField()
    email = models.EmailField(max_length=150)
    date_create = models.DateTimeField(default=timezone.now())

class LinkReseau(models.Model):
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    instagram = models.URLField()
    pinterest = models.URLField()
    date_create = models.DateTimeField(default=timezone.now())
    

class Sold(models.Model):
    days = [
        ("Pizza day", "Pizza day"),
        ("Burger day", "Burger day"),
        ("Pasta day", "Pasta day"),
        ("Fries day", "Fries day"),
    ]
    
    menu_sold = models.ForeignKey(AddMenu, on_delete=models.CASCADE)
    day_special = models.CharField(max_length=25, choices=days)
    reduction = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    date_create = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return str(self.menu_sold)

