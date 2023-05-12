from rest_framework.test import APITestCase
from core.models import Order, Coffee
from django.contrib.auth.models import User


class UserProfileViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test",
            email="testing@test.com",
            password="test1234",
            is_staff=False,
        )
        self.coffee = Coffee.objects.create(
            name="Cafe",
            description="Cafe de grano",
            price=100,
        )
        self.data = {
            "balance": "22",
            "address": "235",
            "city": "La Matanza",
            "state": "Buenos Aires",
            "country": "Argentina",
            "postal_code": "1754",
            "phone": "1234567890",
            "prefered_size": 1,
            "points": 19,
            "status": 1,
            "user": self.user.id,
            "favorite_coffee": self.coffee.id,
        }
        self.client.force_authenticate(user=self.user)

    def test_order_viewset(self):
        response = self.client.post("/api/v1/userprofile/", self.data, format="json")
        self.assertEqual(response.status_code, 201)

        response = self.client.get("/api/v1/userprofile/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["balance"], "22.00")
