"""cafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework import routers

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from api.views import (
    PromotionViewSet,
    CampainViewSet,
    CoffeeViewSet,
    RechargeViewSet,
    UserViewSet,
    UserProfileViewSet,
    OrderViewSet,
    CardViewSet,
)

router = routers.SimpleRouter()

router.register(r"promotion", PromotionViewSet)
router.register(r"campain", CampainViewSet)
router.register(r"coffee", CoffeeViewSet)
router.register(r"recharge", RechargeViewSet)
router.register(r"user", UserViewSet)
router.register(r"userprofile", UserProfileViewSet)
router.register(r"order", OrderViewSet)
router.register(r"card", CardViewSet)

urlpatterns = [
    # YOUR PATTERNS
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path("doc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

urlpatterns += router.urls
