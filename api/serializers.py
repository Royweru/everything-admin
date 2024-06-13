from django.contrib.auth.models import User
from .models import Product
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"
                  ]
        extra_Kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description",
                  "slug", "price", "thumbnail", "images", "creator"]
        extra_kwargs = {"creator": {"read_only": True}}
