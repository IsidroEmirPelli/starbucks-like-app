from rest_framework.test import APITestCase
from core.models import Order, Coffee, UserProfile
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
        self.userprofile = UserProfile.objects.create(
            balance=22,
            address="235",
            city="La Matanza",
            state="Buenos Aires",
            country="Argentina",
            postal_code="1754",
            phone="1234567890",
            prefered_size=1,
            points=19,
            status=1,
            user=self.user,
            role=2,
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
        self.userprofile.role = 1
        self.userprofile.save()
        self.user.save()
        response = self.client.post("/api/v1/order/", self.data, format="json")
        self.assertEqual(response.status_code, 403)
