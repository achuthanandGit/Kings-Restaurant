from django.contrib import admin

from .models import RestaurantMenu, FoodCategory, FoodSubCategory

admin.site.site_header = "Kings Restaurant Dashboard"

# Register your models here.
@admin.register(RestaurantMenu)
class RestaurantMenu(admin.ModelAdmin):
    list_display = ["name", "price", "is_veg", "is_chef_special"]
    list_filter = ["is_veg", "category"]

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(FoodSubCategory)
class FoodSubCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter = ["category"]




