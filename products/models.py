from django.db import models

# Create your models here.
class product(models.Model):
    title = models.TextField()
    decription = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    summary = models.TextField(default='null')
    contact = models.TextField()