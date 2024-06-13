from django.urls import path, include
from .views import ProductListCreate
urlpatterns = [
    path('product/', ProductListCreate.as_view(), name="create-product")
]
