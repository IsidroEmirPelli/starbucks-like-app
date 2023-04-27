from django.db import models


class Recharge(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    mercado_pago_data = models.JSONField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user.username} - {self.card.number} - {self.amount} - {self.date}"
        )

    class Meta:
        verbose_name = "Recharge"
        verbose_name_plural = "Recharges"
