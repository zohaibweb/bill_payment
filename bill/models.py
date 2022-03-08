from django.db import models

# Create your models here.
class Bnda(models.Model):
    name = models.CharField(max_length=50, blank=False)
    bill = models.IntegerField(default=250)
    paidDate = models.DateField()

    