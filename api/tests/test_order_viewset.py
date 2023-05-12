from rest_framework.test import APITestCase
from core.models import Order, Coffee
from django.contrib.auth.models import User


class OrderViewSetTestCase(APITestCase):
    def setUp(self):
        self.coffee = Coffee.objects.create(
            name="Cafe",
            description="Cafe de grano",
            price=100,
        )
        self.user = User.objects.create(
            username="test",
            email="testing@test.com",
            password="test1234",
            is_staff=True,
        )
        self.client.force_authenticate(user=self.user)
        self.data = {
            "buys": [
                {
                    "quantity": 1,
                    "size": 1,
                    "price": "10",
                    "user": self.user.id,
                    "coffee": self.coffee.id,
                },
                {
                    "quantity": 1,
                    "size": 1,
                    "price": "10",
                    "user": self.user.id,
                    "coffee": self.coffee.id,
                },
            ],
            "total_price": "10",
            "user": self.user.id,
        }

    def test_order_viewset(self):
        response = self.client.post("/api/v1/order/", self.data, format="json")
        print(response)
        self.assertEqual(response.status_code, 201)

        response = self.client.get("/api/v1/order/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data[0]["buys"]), 2)

    def test_order_viewset_without_staff(self):
        self.user.is_staff = False
        self.user.save()
        response = self.client.post("/api/v1/order/", self.data, format="json")
        self.assertEqual(response.status_code, 403)
