from django.db import models


class Coffee(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="coffees", null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.price} - {self.description} - {self.image} - {self.creation_date} - {self.last_update}"

    class Meta:
        verbose_name = "Coffee"
        verbose_name_plural = "Coffees"
