from rest_framework import generics

from menu.models import Food
from menu.serializers import FoodSerializer, FoodListSerializer


class FoodCreateAPIView(generics.CreateAPIView):
    """ Создание товара """

    serializer_class = FoodSerializer

    def perform_create(self, serializer):
        """ Определяем порядок создания нового объекта """

        new_product = serializer.save()
        new_product.save()


class FoodListAPIView(generics.ListAPIView):
    """ Вывод списка блюд """

    serializer_class = FoodListSerializer

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Food.objects.all()
        return queryset
