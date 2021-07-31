from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField('Название', max_length=250)
    start_date = models.DateField('Дата начала')
    stop_date = models.DateField('Дата окончания')
    description = models.TextField('Описание')

    def __str__(self):
        return  self.title


    class Meta:
        verbose_name = 'Опрос   '
