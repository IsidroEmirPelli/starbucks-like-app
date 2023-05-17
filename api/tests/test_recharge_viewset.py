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


MP_RESPONSE_BAD = {
    "status": 400,
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


class OrderViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test",
            email="testing@test.com",
            password="test1234",
            is_staff=True,
        )
        self.client.force_authenticate(user=self.user)

    def create_order(self, user):
        data = {
            "amount": "22",
            "token": "ada",
            "installments": 2,
            "payment_method_id": "2",
            "identification_type": "2",
            "identification_number": "1",
            "user": user.id,
        }

        response = self.client.post("/api/v1/recharge/", data, format="json")
        return response

    def test_order_viewset(self):
        def mock_create_payment(recharge):
            return MP_RESPONSE

        monkeypatch = pytest.MonkeyPatch()
        monkeypatch.setattr("api.views.create_payment", mock_create_payment)

        response = self.create_order(self.user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, MP_RESPONSE)

    def test_order_viewset_status_bad(self):
        def mock_create_payment(recharge):
            return MP_RESPONSE_BAD

        monkeypatch = pytest.MonkeyPatch()
        monkeypatch.setattr("api.views.create_payment", mock_create_payment)

        response = self.create_order(self.user)
        self.assertEqual(response.status_code, 400)

    def test_add_other_user(self):
        def mock_create_payment(recharge):
            return MP_RESPONSE

        monkeypatch = pytest.MonkeyPatch()
        monkeypatch.setattr("api.views.create_payment", mock_create_payment)

        user = User.objects.create(
            username="test1",
            email="testing1@test.com",
            password="test1234",
        )
        self.client.force_authenticate(user=user)
        response = self.create_order(user)
        self.assertEqual(response.status_code, 201)

        response = self.client.get("/api/v1/recharge/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        self.client.force_authenticate(user=self.user)
        for i in range(2):
            response = self.create_order(self.user)
            self.assertEqual(response.status_code, 201)
        response = self.client.get("/api/v1/recharge/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_order_viewset_with_recharge_none(self):
        def mock_create_payment(recharge):
            return None

        monkeypatch = pytest.MonkeyPatch()
        monkeypatch.setattr("api.views.create_payment", mock_create_payment)
        response = self.create_order(self.user)
        self.assertEqual(response.status_code, 400)
        assert response.data["error"] != ""

    def test_order_viewset_with_user_not_logged(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/v1/recharge/")
        self.assertEqual(response.status_code, 403)
