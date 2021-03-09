from django.db import models

# Create your models here.




class PersionDetails(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    choice_gender = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(choices=choice_gender, max_length=10)

    def __str__(self):
        return self.name