from django.db import models

# Create your models here.

class Noodle(models.Model):

    name= models.CharField(max_length=30)
    img= models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

