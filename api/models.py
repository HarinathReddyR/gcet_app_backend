from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Dept(models.Model):
    bcode = models.CharField(primary_key = True, max_length = 255)
    bname = models.CharField(max_length=255)

class Student(models.Model):
    rollno = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    stdName = models.CharField(max_length=255)
    branch = models.ForeignKey(Dept, on_delete=models.CASCADE)
    section = models.CharField(max_length=255)
    year = models.IntegerField()
    sem = models.IntegerField()




class Faculty(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    facultyName = models.CharField(max_length=255)
# Create your models here.
