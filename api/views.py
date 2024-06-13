from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ProductSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Product
# Create your views here.


class CreateUserView(generics.CreateAPIView):
    querySet = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        if self.request.method == "GET":
            return Product.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
