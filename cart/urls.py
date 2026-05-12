from django.urls import path
from .views import (
    my_cart,
    add_to_cart,
    update_cart_item,
    remove_from_cart,
    clear_cart
)

urlpatterns = [
    path('', my_cart),
    path('add/', add_to_cart),

    path('update/<int:pk>/', update_cart_item),
    path('remove/<int:pk>/', remove_from_cart),
    path('clear/', clear_cart),
]