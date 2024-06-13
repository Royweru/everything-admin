from django.urls import path, include
from .views import ProductListCreate
urlpatterns = [
    path('list/', ProductListCreate.as_view(), name="create-product")
]
