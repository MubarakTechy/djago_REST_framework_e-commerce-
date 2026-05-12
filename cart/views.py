from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Cart, CartItem
from .serializers import CartSerializer

from products.models import Product


# GET USER CART
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_cart(request):

    user = request.user

    cart, created = Cart.objects.get_or_create(user=user)

    serializer = CartSerializer(cart)

    return Response(serializer.data)


# ADD TO CART
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):

    user = request.user

    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)

    # validation
    if not product_id:
        return Response(
            {"error": "product_id is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # get or create cart
    cart, created = Cart.objects.get_or_create(user=user)

    # get or create cart item
    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not item_created:
        cart_item.quantity += int(quantity)
    else:
        cart_item.quantity = int(quantity)

    cart_item.save()

    serializer = CartSerializer(cart)

    return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_cart_item(request, pk):

    try:
        cart_item = CartItem.objects.get(id=pk)
    except CartItem.DoesNotExist:
        return Response(
            {"error": "Cart item not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    quantity = request.data.get('quantity')

    if not quantity:
        return Response(
            {"error": "Quantity is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    cart_item.quantity = quantity
    cart_item.save()

    serializer = CartSerializer(cart_item.cart)

    return Response(serializer.data)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, pk):

    try:
        cart_item = CartItem.objects.get(id=pk)
    except CartItem.DoesNotExist:
        return Response(
            {"error": "Cart item not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    cart = cart_item.cart

    cart_item.delete()

    serializer = CartSerializer(cart)

    return Response(serializer.data)




@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def clear_cart(request):

    user = request.user

    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        return Response(
            {"error": "Cart not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    cart.items.all().delete()

    return Response({
        "message": "Cart cleared successfully"
    })