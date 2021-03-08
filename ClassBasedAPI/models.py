from django.db import models

# Create your models here.


class Persion(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    choice_gender = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(choices=choice_gender, max_length=10)

    def __str__(self):
        return self.name
