from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Faculty(models.Model):
    Name = models.CharField(max_length=50)
    Contact = models.IntegerField(null=True)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Student(models.Model):
    Name = models.CharField(max_length=50)
    Contact = models.IntegerField(null=True)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Administrative(models.Model):
    Name = models.CharField(max_length=50)
    Contact = models.IntegerField(null=True)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Name