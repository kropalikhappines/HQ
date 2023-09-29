from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UsersModel, ProductsModel, LessonsModel, Access
from .serializers import UsersModelSerializer, ProductsModelSerializer, LessonsModelSerializer


class UsersModelViewSet(ModelViewSet):
    """Базовое представление пользователя"""
    queryset = UsersModel.objects.all()
    serializer_class = UsersModelSerializer


class ProductModelViewSet(ModelViewSet):
    """Базовое представление продукта"""
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsModelSerializer


class LessonsModelViewSet(ModelViewSet):
    """Базовое представление урока"""
    queryset = LessonsModel.objects.all()
    serializer_class = LessonsModelSerializer


class UserProductList(generics.ListAPIView):
    """Представление листа продуктов пользователя"""
    serializer_class = ProductsModelSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']  # Получить user_id из URL
        return ProductsModel.objects.filter(owner=user_id)


class UserLessonList(generics.ListAPIView):
    """Представление листа уроков пользователя"""
    serializer_class = LessonsModelSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']  # Получить user_id из URL
        return LessonsModel.objects.filter(owner=user_id)
