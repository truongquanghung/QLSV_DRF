from django.db import models

# Create your models here.
class student(models.Model):
    GENDER_CHOICES = (('Nam', 'Nam'),('Nữ', 'Nữ'))
    mssv = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=5, choices=GENDER_CHOICES)
    faculty = models.CharField(max_length=500)

    def __str__(self):
        return self.name