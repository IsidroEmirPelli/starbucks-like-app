from django.db import models


class Promotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    percentaje = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    coffee_related = models.ManyToManyField("core.Coffee", null=True, blank=True)
    expire_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField("auth.User", related_name="promotions")
    filters = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.description} - {self.creation_date} - {self.last_update}"

    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"
