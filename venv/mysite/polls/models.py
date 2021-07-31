from django.db import models

# Create your models here.
class Survey(models.Model):
    title = models.CharField('Название', max_length=250)
    start_date = models.DateTimeField('Дата начала')
    stop_date = models.DateTimeField('Дата окончания')
    description = models.TextField('Описание')


    def __str__(self):
        return self.name


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete= models.CASCADE)
    text_question = models.TextField('Текст вопроса')
    type_question = models.TextField('Тип вопроса', help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")


    def __str__(self):
        return  self.title


    class Meta:
        verbose_name = "Опрос"