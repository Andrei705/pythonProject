from django.contrib import admin

from .models import SurveyAttributes, QuestionAttributes, Answer

# Register your models here.

admin.site.register(SurveyAttributes)

admin.site.register(QuestionAttributes)

admin.site.register(Answer)

