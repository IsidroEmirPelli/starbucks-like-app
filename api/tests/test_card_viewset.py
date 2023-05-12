from rest_framework.test import APITestCase
from core.models import Order, Coffee
from django.contrib.auth.models import User


class CardViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test",
            email="testing@test.com",
            password="test1234",
            is_staff=False,
        )
        self.data = {
            "number": "2222222",
            "user": self.user.id,
        }
        self.client.force_authenticate(user=self.user)

    def test_order_viewset(self):
        response = self.client.post("/api/v1/card/", self.data, format="json")
        self.assertEqual(response.status_code, 201)

        response = self.client.get("/api/v1/card/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["number"], "2222222")
