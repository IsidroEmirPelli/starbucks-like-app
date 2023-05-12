from rest_framework.test import APITestCase
from django.contrib.auth.models import User
import pytest

MP_RESPONSE = {
    "status": "approved",
    "status_detail": "accredited",
    "id": 3055677,
    "date_approved": "2019-02-23T00:01:10.000-04:00",
    "payer": {
        "type": "customer",
    },
    "payment_method_id": "visa",
    "payment_type_id": "credit_card",
    "refunds": [],
}


class OrderviewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test",
            email="testing@test.com",
            password="test1234",
            is_staff=True,
        )
        self.client.force_authenticate(user=self.user)
        self.data = {
            "amount": "22",
            "token": "ada",
            "installments": 2,
            "payment_method_id": "2",
            "identification_type": "2",
            "identification_number": "1",
            "user": self.user.id,
        }

    def test_order_viewset(self):
        def mock_create_payment(recharge):
            return MP_RESPONSE

        monkeypatch = pytest.MonkeyPatch()
        monkeypatch.setattr("api.views.create_payment", mock_create_payment)

        response = self.client.post("/api/v1/recharge/", self.data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, MP_RESPONSE)
