from django.db import models
from django.contrib.auth.models import User

class Tasks (models.Model):
    task_name = models.CharField('Имя задачи', max_length=50)
    task_description = models.CharField('Описание задачи', max_length=50)
    date_create = models.DateTimeField('Дата создания задачи')
    execution_status = models.CharField('Статус выполнения', max_length=50)
    date_execution = models.DateTimeField('Дата выполнения задачи')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'