from django.urls import path, include
from .views import ProductListCreate, ProductDelete, ProductUpdate, UserDetail, ProductRetrieve, CategoryListCreate
urlpatterns = [
    path('product/', ProductListCreate.as_view(), name="create-product"),
    path('category/', CategoryListCreate.as_view(), name="create-category "),
    path('product/<str:pk>/', ProductRetrieve.as_view(), name="get-product"),
    path('product/delete/<str:pk>/',
         ProductDelete.as_view(), name='product-delete'),
    path('product/update/<str:pk>/',
         ProductUpdate.as_view(), name='product-update'),
    path('user/', UserDetail.as_view(), name="user-details")
]
