from django.db import models

# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return self.name
