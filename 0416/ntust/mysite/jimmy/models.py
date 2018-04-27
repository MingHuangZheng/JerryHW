from django.db import models

# Create your models here.
class Information(models.Model):
    name = models.CharField(max_length=15)
    birthday = models.CharField(max_length=8)
    gender = models.CharField(max_length=5)

    def __str__(self):
        return self.name


