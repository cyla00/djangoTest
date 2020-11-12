from django.db import models
# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    summary = models.TextField(default='null')
    

    def __str__(self):
        return self.title