from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.TextField()

    def __str__(self):
        return self.name + " - " + self.email
