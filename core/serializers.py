from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Campain, Card, Coffee, Promotion, Recharge, UserProfile, Order, Buy


class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    buys = BuySerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        buys_data = validated_data.pop("buys")
        order = Order.objects.create(**validated_data)

        for buy_data in buys_data:
            order.buys.add(Buy.objects.create(**buy_data))
        return order


class CampainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campain
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = "__all__"


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = (
            "name",
            "description",
            "creation_date",
            "filters",
            "percentaje",
            "coffee_related",
            "expire_date",
        )
        read_only_fields = ("users",)


class RechargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recharge
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name", "last_name")
