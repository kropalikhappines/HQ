from rest_framework import serializers
from .models import UsersModel, ProductsModel, LessonsModel, Access


class UsersModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsersModel
        fields = "__all__"


class ProductsModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductsModel
        fields = "__all__"


class LessonsModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LessonsModel
        fields = "__all__"
