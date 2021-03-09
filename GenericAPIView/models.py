from django.db import models

# Create your models here.

class Admission(models.Model):
    name = models.CharField(max_length=50),
    university_name = models.CharField(max_length=50)
    admission_fee = models.IntegerField()

    def __str__(self):
        return self.name



