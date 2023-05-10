from django.db import models


class Recharge(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    token = models.CharField(max_length=100, null=True, blank=True)
    installments = models.IntegerField(default=0)
    payment_method_id = models.CharField(max_length=100, null=True, blank=True)
    identification_type = models.CharField(max_length=100, null=True, blank=True)
    identification_number = models.CharField(max_length=100, null=True, blank=True)
    mercado_pago_data = models.JSONField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.date}"

    class Meta:
        verbose_name = "Recharge"
        verbose_name_plural = "Recharges"
