from django.urls import path

from .views import (
    product_list,
    create_product,
    get_product,
    update_product,
    delete_product
)

urlpatterns = [
    path('', product_list),  # GET ALL PRODUCTS
    path('create/', create_product),
    path('<int:pk>/', get_product),  # SINGLE PRODUCT
    path('<int:pk>/update/', update_product),
    path('<int:pk>/delete/', delete_product),
]