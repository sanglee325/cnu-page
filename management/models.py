from django.db import models

# Create your models here.
class Manager(models.Model):
    student = models.CharField(max_length=20)

class Period(models.Model):
    student1 = Manager()
    student2 = Manager()

    