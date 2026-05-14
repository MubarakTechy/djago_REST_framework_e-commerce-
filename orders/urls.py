from django.urls import path

from .views import (
    CheckoutView,
    OrderHistoryView,
    OrderDetailView
)
from .views import InitializePaymentView

urlpatterns = [
    path('checkout/', CheckoutView.as_view()),
    path('', OrderHistoryView.as_view()),
    path('<int:pk>/', OrderDetailView.as_view()),
    path('initialize-payment/<int:pk>/', InitializePaymentView.as_view()),
    
]