from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    auther = models.CharField(max_length=50)
    email = models.EmailField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str(self):
        return self.title

