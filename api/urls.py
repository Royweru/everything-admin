from django.urls import path
from .views import ProductListCreate, CategoryDetailView, ProductDelete, ProductUpdate, UserDetail, ProductRetrieve, EmailMessageCreate, CategoryListCreate
urlpatterns = [
    path('product/', ProductListCreate.as_view(), name="create-product"),
    path('email-message/', EmailMessageCreate.as_view(), name='create-email '),
    path('category/<int:id>/', CategoryDetailView.as_view(),
         name='category-detail'),
    path('category/', CategoryListCreate.as_view(), name="create-category "),
    path('product/<str:pk>/', ProductRetrieve.as_view(), name="get-product"),
    path('product/delete/<str:pk>/',
         ProductDelete.as_view(), name='product-delete'),
    path('product/update/<str:pk>/',
         ProductUpdate.as_view(), name='product-update'),
    path('user/', UserDetail.as_view(), name="user-details")
]
