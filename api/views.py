from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from core.permissions import AdminPermission
from core.models import Order, Campain, Card, Coffee, Promotion, Recharge, UserProfile
from core.utils import create_payment
from core.serializers import (
    OrderSerializer,
    CampainSerializer,
    CardSerializer,
    CoffeeSerializer,
    PromotionSerializer,
    RechargeSerializer,
    UserSerializer,
    UserProfileSerializer,
)

# Create your views here.
class PromotionViewSet(viewsets.ModelViewSet):
    """Viewset for promotion's model"""

    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [AdminPermission, IsAuthenticated]


class UserProfileViewSet(viewsets.ModelViewSet):
    """Viewset for user profile model"""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AdminPermission, IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class RechargeViewSet(viewsets.ModelViewSet):
    """Viewset for recharge model"""

    queryset = Recharge.objects.all()
    serializer_class = RechargeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        recharge = super().create(request, *args, **kwargs)
        recharge = recharge.data
        recharge = Recharge.objects.get(id=recharge["id"])
        try:
            response = create_payment(recharge)
            if response["status"] == 400:
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            recharge.mercado_pago_data = response
            recharge.save()
            return Response(recharge.mercado_pago_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(viewsets.ModelViewSet):
    """Viewset for order model"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Viewset For Order Model
        Example of request:
        {
        "buys": [
            {
            "quantity": 100,
            "size": 1,
            "price": "25.00",
            "user": 0,
            "coffee": 0
            }
        ],
        "total_price": "string",
        "user": 0
        }
        """
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class CampainViewSet(viewsets.ModelViewSet):
    queryset = Campain.objects.all()
    serializer_class = CampainSerializer
    permission_classes = [AdminPermission, IsAuthenticated]


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class CoffeeViewSet(viewsets.ModelViewSet):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer
    permission_classes = [AdminPermission, IsAuthenticated]


class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminPermission, IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.data["is_staff"] == "true":
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)
