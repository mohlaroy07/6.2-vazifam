from django.contrib import admin
from .models import FoodType, Food, Comment

admin.site.register(FoodType)
admin.site.register(Food)
admin.site.register(Comment)
