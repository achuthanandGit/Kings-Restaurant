from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .models import RestaurantMenu, FoodCategory, FoodSubCategory
from .kings_service import view_service as service

"""
home will load the web page with all necessary data

"""
def home(request):
    restaurant_menu_list = RestaurantMenu.objects.all()
    special_menu_list = restaurant_menu_list.filter(is_chef_special=True)
    template = "kingsres/home.html"
    context = {
        "menu_list": service.arrange_food_menu(service.group_menu_list(restaurant_menu_list)),
        "special_menu_list": special_menu_list,
    }
    return render(request, template, context)

def customer_order(request):
    return render(request, 'kingsres/order.html', {})
