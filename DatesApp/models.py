from django.db import models
from datetime import datetime

# Create your models here.

class TasksDate(models.Model):

    date = models.DateField(default=datetime.now, auto_now_add=False)
    is_published = models.BooleanField(default=True, verbose_name='Рабочий день')

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural = "Даты"