from rest_framework.test import APITestCase
from core.models import Order, Coffee
from django.contrib.auth.models import User


class UserViewSetTestCase(APITestCase):
    def setUp(self):
        self.data = {
            "username": "isidro",
            "email": "user@example.com",
            "password": "123456",
            "first_name": "isidro",
            "last_name": "pelli",
        }

    def test_user_viewset(self):
        response = self.client.post("/api/v1/user/", self.data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_user_viewset_with_is_staff(self):
        self.data["username"] = "isidro2"
        self.data["email"] = "user1@example.com"
        self.data["is_staff"] = True
        response = self.client.post("/api/v1/user/", self.data, format="json")
        self.assertEqual(response.status_code, 403)
