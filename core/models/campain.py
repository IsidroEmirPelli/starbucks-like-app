from django.db import models


class Campain(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, default="")
    html_content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    promotion_related = models.ForeignKey(
        "core.Promotion", on_delete=models.CASCADE, null=True, blank=True
    )
    users = models.ManyToManyField("auth.User", related_name="campains")
    objective_date = models.DateTimeField()
    filters = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.creation_date} - {self.last_update} - {self.objective_date}"

    class Meta:
        verbose_name = "Campain"
        verbose_name_plural = "Campains"
