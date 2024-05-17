from datetime import datetime

from django.db import models

# Create your models here.
class ToDo(models.Model):
    detail = models.CharField(max_length=100)
    check_do  = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.detail
