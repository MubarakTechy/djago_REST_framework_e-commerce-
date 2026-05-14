from django.urls import path

from .views import (
    CheckoutView,
    OrderHistoryView,
    OrderDetailView
)

urlpatterns = [
    path('checkout/', CheckoutView.as_view()),
    path('', OrderHistoryView.as_view()),
    path('<int:pk>/', OrderDetailView.as_view()),
]