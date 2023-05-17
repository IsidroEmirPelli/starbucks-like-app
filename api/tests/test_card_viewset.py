from rest_framework.test import APITestCase
from core.models import Order, Coffee, UserProfile
from django.contrib.auth.models import User


class CardViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test",
            email="testing@test.com",
            password="test1234",
            is_staff=False,
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
            role=1,
        )
        self.data = {
            "user": self.user.id,
        }
        self.client.force_authenticate(user=self.user)

    def test_card_viewset(self):
        response = self.client.post("/api/v1/card/", self.data, format="json")
        self.assertEqual(response.status_code, 201)

        response = self.client.get("/api/v1/card/")
        print(response.data)
        self.assertEqual(response.status_code, 200)
        assert "number" in response.data[0]
