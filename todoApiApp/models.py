from django.db import models

# Create your models here.

class Todo(models.Model):
    body = models.CharField(verbose_name='body',max_length=1024)
    date = models.DateField(verbose_name='date')
