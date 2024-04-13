from django.urls import path

from menu.apps import MenuConfig
from menu.views import FoodListAPIView

app_name = MenuConfig.name


urlpatterns = [
    path('foods/', FoodListAPIView.as_view(), name='foods_list'),
]
