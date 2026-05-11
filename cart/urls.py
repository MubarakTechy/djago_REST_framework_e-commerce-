from django.urls import path

from .views import my_cart

urlpatterns = [
    path('my-cart/', my_cart),
]