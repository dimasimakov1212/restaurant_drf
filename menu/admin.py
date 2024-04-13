from django.contrib import admin

from menu.models import FoodCategory, Food

admin.site.register(FoodCategory, Food)
