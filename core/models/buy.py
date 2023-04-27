from django.db import models
from django_enumfield import enum

from core.common import Size


class Buy(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    coffee = models.ForeignKey("core.Coffee", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=10, choices=Size.choices(), default=Size.SMALL)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.coffee.name} - {self.quantity} - {self.size} - {self.price} - {self.date}"

    class Meta:
        verbose_name = "Buy"
        verbose_name_plural = "Buys"
