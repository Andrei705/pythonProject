from django.db import models

# Create your models here.

class Object_folder(models.Model):
    name = models.CharField('Папка', max_length=100)
    name_films = models.CharField('Название фильма', max_length=100)
    name_cinema = models.CharField('Название кинотеатра', max_length=100)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Заполнение данными'

# class filing_folder(models.Model):
#     folder = models.ForeignKey(Object_folder,on_delete=models.PROTECT)