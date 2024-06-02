from django.urls import path, include
from . import views

urlpatterns = [
    path("product", views.product_list, name='index'),
    path("product/<int:pk>", views.product_detail, name='detail'),
    path("product/create", views.product_create, name='create'),
    path("product/update/<int:pk>", views.product_update, name='update'),
    path("product/delete/<int:pk>", views.product_delete, name='delete')
]

