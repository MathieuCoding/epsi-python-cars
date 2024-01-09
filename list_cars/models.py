from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.IntegerField()
    engine = models.CharField(max_length=200)
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.brand + ' - ' + self.model + ' - ' + self.engine