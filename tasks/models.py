from django.db import models
from django.contrib.auth.models import User

class Tasks (models.Model):
    name = models.CharField('Имя задачи', max_length=50)
    description = models.CharField('Описание задачи', max_length=200)
    date_create = models.DateTimeField('Дата создания задачи')
    deadline = models.CharField('Срок выполнения задачи', max_length=50)
    execution_status = models.CharField('Статус выполнения', max_length=50, null=True, blank=True, default="Ожидает выполнения")
    date_execution = models.DateTimeField('Дата выполнения задачи', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/tasks'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'