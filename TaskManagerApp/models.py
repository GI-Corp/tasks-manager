from django.db import models
from datetime import datetime
from DatesApp.models import TasksDate


# Create your models here.

class Tasks(models.Model):

    first = "Поручение"
    second = "Письмо"
    third = "Обращение"
    fourth = "Фишка"


    CATEGORY_CHOICES = [
        (first, "Поручение"),
        (second, "Письмо"),
        (third, "Обращение"),
        (fourth, "Фишка"),
    ]

    # Date info
    date = models.ForeignKey(TasksDate, on_delete=models.SET_NULL, verbose_name='Сегодняшняя дата', related_name='specific_date', null=True)
    # Task details
    category = models.CharField(max_length=500, choices=CATEGORY_CHOICES, null=True, blank=True, verbose_name='Вид')
    sign = models.CharField(max_length=300, verbose_name='Подпись', null=True, blank=True)
    contract_id_unique = models.CharField(max_length=500, unique=True, verbose_name='Номер', blank=True, null=True, help_text='Номер не должен повторяться')
    task_date = models.DateField(verbose_name='Дата', blank=True, null=True)
    content = models.CharField(max_length=700, verbose_name='Содержание', null=True, blank=True)
    responsible_user = models.CharField(max_length=300, verbose_name='Исполнитель', null=True, blank=True)
    task_deadline = models.DateField(verbose_name='Дата', blank=True, null=True)
    result = models.CharField(max_length=300, verbose_name='Результат', help_text='Для начальника', null=True, blank=True)
    verification = models.CharField(max_length=500, verbose_name='Отметка', null=True, blank=True)
   
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать задачу')

    def __str__(self):
        return self.contract_id_unique

    class Meta:
        verbose_name_plural = "Список дел"
