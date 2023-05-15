from django.db import models

# Create your models here.


class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    exception = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Issue"
        verbose_name_plural = "Issues"

    def __str__(self):
        return f"{self.title} - {self.created_at}"
