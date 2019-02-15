from django.db import models
from django.utils import timezone

class Person(models.Model):
    name = models.CharField(max_length=20)
    student_number = models.CharField(max_length=10)
    birthday = models.DateField(default=timezone.now, blank=True)
    email = models.CharField(max_length=50, default=None)
    github = models.URLField(max_length=200, default=None)

    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', '---')
    )
    joined_date = models.DateTimeField(default=timezone.now)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='X')

    def join(self):
        self.joined_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name