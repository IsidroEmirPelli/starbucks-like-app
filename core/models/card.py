from django.db import models

class Card(models.Model):
    number = models.CharField(max_length=19)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_use = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.number} - {self.balance} - {self.creation_date} - {self.last_use}"
    
    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"
        