from django.db import models

class TripIncome(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.amount}"
