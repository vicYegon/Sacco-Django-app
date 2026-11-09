from django.db import models

# Create your models here.
class Member(models.Model):
    full_name = models.CharField(max_length=150)
    national_id = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    monthly_contribution = models.DecimalField(max_digits=12, decimal_places=2)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name