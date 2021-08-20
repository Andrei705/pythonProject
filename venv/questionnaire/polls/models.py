from django.db import models

# Create your models here.

class SurveyAttributes(models.Model):
    name = models.TextField('Название')
    date_start = models.DateField('Дата старта')
    date_stop = models.DateField('Дата окончания')
    description = models.TextField('Описание')


    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


    def __str__(self):
        return self.name


class QuestionAttributes(models.Model):
    survey = models.ForeignKey(SurveyAttributes, on_delete=models.CASCADE)
    txt_question = models.TextField('Текст вопроса')
    typ_question = models.TextField('Тип вопроса')


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


    def __str__(self):
        return self.txt_question


class Answer(models.Model):
    question = models.ForeignKey(QuestionAttributes,on_delete=models.CASCADE)
    txt_answer = models.TextField('Ответ текстом')