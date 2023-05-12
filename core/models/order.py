from django.db import models
from django_enumfield import enum
from django.core.validators import MinValueValidator, MaxValueValidator


class Order(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    buys = models.ManyToManyField(
        "core.Buy", related_name="orders", blank=True, null=True
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100000)],
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.total_price} - {self.date}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
