from django.contrib.auth.models import User
from .models import Product, Email_messages, Category
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
    category_id = serializers.IntegerField(write_only=True)
    category = serializers.CharField(read_only=True, source='category.name')

    class Meta:
        model = Product
        fields = ["id", "name", "description",
                  "slug", "price", "thumbnail", "images", "creator", "category_id", 'category']
        extra_kwargs = {"creator": {"read_only": True}}

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        category = Category.objects.get(id=category_id)
        product = Product.objects.create(category=category, **validated_data)
        return product


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "products"]


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"
                  ]
        extra_Kwargs = {"password": {"write_only": True}}


class EmailMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email_messages
        fields = ['id', 'name', 'email', 'message']

    def create(self, validated_data):
        email = Email_messages.objects.create(**validated_data)
        return email
