from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

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
    permission_classes = []
