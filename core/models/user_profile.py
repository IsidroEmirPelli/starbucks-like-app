from django.db import models
from django_enumfield import enum
from django.core.validators import MinValueValidator, MaxValueValidator

from core.common import Size, Status

# Create your models here.


class UserProfile(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    favorite_coffee = models.ForeignKey(
        "core.Coffee", on_delete=models.CASCADE, null=True, blank=True
    )
    prefered_size = enum.EnumField(Size, default=Size.SMALL)
    points = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100000)]
    )
    status = enum.EnumField(Status, default=Status.ACTIVE)

    def __str__(self):
        return f"{self.user.username} - {self.address} - {self.city} - {self.state} - {self.country} - {self.postal_code} - {self.phone}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
