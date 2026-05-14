from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from cart.models import CartItem
from .models import Order, OrderItem
from .serializers import OrderSerializer


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        cart_items = CartItem.objects.filter(
            user=request.user
        )

        if not cart_items.exists():
            return Response({
                "message": "Cart is empty"
            })

        total_price = 0

        order = Order.objects.create(
            user=request.user
        )

        for item in cart_items:

            price = item.product.price * item.quantity

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=price
            )

            total_price += price

        order.total_price = total_price
        order.save()

        # Clear cart
        cart_items.delete()

        serializer = OrderSerializer(order)

        return Response(serializer.data)

class OrderHistoryView(ListAPIView):

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user
        ).order_by('-created_at')
    

class OrderDetailView(RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user
        )