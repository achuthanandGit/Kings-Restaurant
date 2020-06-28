from django.db import models

# Create your models here.
class RestaurantMenu(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    category = models.ForeignKey(to="FoodCategory", on_delete=models.CASCADE)
    sub_category = models.ForeignKey(to="FoodSubCategory", on_delete=models.CASCADE, blank=True)
    is_veg = models.BooleanField(default=False)
    is_chef_special = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images')


class FoodCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        
class FoodSubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(to="FoodCategory", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name



