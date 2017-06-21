from django.db import models

# Create your models here.
class Information(models.Model):
            name= models.CharField(max_length=20)
            age = models.CharField(max_length=3)
            sex = models.CharField(max_length=2)
            grade = models.CharField(max_length=10)
            major = models.CharField(max_length=30)
            personinformation = models.CharField(max_length=100)
            def __str__(self):
                return self.name


class Admincheck(models.Model):
        admin = models.CharField(max_length=10)
        password = models.CharField(max_length=10)
        def __str__(self):
            return self.name