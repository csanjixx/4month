from django.urls import path
from .views import edit_product

urlpatterns = [
    path('products/<int:pk>/edit/', edit_product, name='edit_product'),
]