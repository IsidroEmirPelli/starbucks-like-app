from rest_framework import serializers

from .models import Buy, Campain, Card, Coffee, Promotion, Recharge, UserProfile


class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = "__all__"


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
