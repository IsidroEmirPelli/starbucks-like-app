from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from core.permissions import AdminPermission
from core.models import Buy, Campain, Card, Coffee, Promotion, Recharge, UserProfile
from core.serializers import (
    BuySerializer,
    CampainSerializer,
    CardSerializer,
    CoffeeSerializer,
    PromotionSerializer,
    RechargeSerializer,
    UserProfileSerializer,
)

# Create your views here.
class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [AdminPermission, IsAuthenticated]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AdminPermission, IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class RechargeViewSet(viewsets.ModelViewSet):
    queryset = Recharge.objects.all()
    serializer_class = RechargeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class BuyViewSet(viewsets.ModelViewSet):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
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
