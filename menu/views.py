from rest_framework import generics

from menu.models import Food, FoodCategory
from menu.serializers import FoodListSerializer
from django.db.models import Prefetch


class FoodListAPIView(generics.ListAPIView):
    """ Вывод списка блюд """

    serializer_class = FoodListSerializer

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        # получаем опубликованные объекты продуктов
        foods = Food.objects.filter(is_publish=True)

        # получаем категории, в которых есть хотя бы один опубликованный продукт
        queryset = FoodCategory.objects.filter(food__is_publish=True).distinct()

        # делаем предварительную загрузку связанных объектов
        prefetch_filtered_foods = Prefetch('food', foods)

        # переопределяем параметры вывода объектов
        queryset = queryset.prefetch_related(prefetch_filtered_foods)

        return queryset
