import os
import mercadopago


def create_payment(recharge):
    access_token = os.environ.get("MERCADOPAGO_ACCESS")
    sdk = mercadopago.SDK(access_token)
    payment_data = {
        "transaction_amount": float(recharge.amount),
        "token": recharge.token,
        "description": "Recarga de saldo",
        "installments": recharge.installments,
        "payment_method_id": recharge.payment_method_id,
        "payer": {
            "email": recharge.user.email,
            "identification": {
                "type": recharge.identification_type,
                "number": recharge.identification_number,
            },
        },
    }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]

    return payment
