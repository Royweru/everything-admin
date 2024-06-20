from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, ProductSerializer, UserDetailsSerializer, CategorySerializer, EmailMessageSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Product, Category, Email_messages
# Create your views here.


class CreateUserView(generics.CreateAPIView):
    querySet = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class EmailMessageCreate(generics.CreateAPIView):
    queryset = Email_messages.objects.all()
    serializer_class = EmailMessageSerializer
    permission_classes = [AllowAny]


class CategoryListCreate(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        if self.request.method == "GET":
            return Category.objects.all()
        else:
            user = self.request.user
            return Category.objects.filter(creator=user)


class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    lookup_field = 'id'


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
        else:
            user = self.request.user
            return Product.objects.filter(creator=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(creator=self.request.user)
        else:
            print(serializer.errors)


class ProductRetrieve(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ProductDelete(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.method == "GET":
            return Product.objects.all()
        else:
            user = self.request.user
            return Product.objects.filter(creator=user)


class ProductUpdate(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(creator=user)

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserDetailsSerializer(user)
        return Response(serializer.data)
