from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from .models import Cart
from .serializers import CartSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_cart(request):

    user = request.user

    cart = Cart.objects.filter(user=user)

    serializer = CartSerializer(cart, many=True)

    return Response(serializer.data)