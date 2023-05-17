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

    def test_try_update_user_not_logged(self):
        user_created = User.objects.create(
            username="test",
            email="user@example.com",
            password="test1234",
            is_staff=False,
        )
        data = {
            "username": "isidro",
            "password": "123456",
        }
        self.client.force_authenticate(user=None)
        response = self.client.put(
            f"/api/v1/user/{user_created.id}/", data, format="json"
        )
        self.assertEqual(response.status_code, 403)

    def test_try_partial_update_user_not_logged(self):
        user_created = User.objects.create(
            username="test",
            email="user@example.com",
            password="test1234",
            is_staff=False,
        )
        data = {
            "username": "isidro",
            "password": "123456",
        }
        self.client.force_authenticate(user=None)
        response = self.client.patch(
            f"/api/v1/user/{user_created.id}/", data, format="json"
        )
        self.assertEqual(response.status_code, 403)
