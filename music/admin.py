from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Mbti)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['a_type', 'a_text', 'question_n']


admin.site.register(models.Answer, AnswerAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['q_number', 'q_title']


admin.site.register(models.Question, QuestionAdmin)


class MTextAdmin(admin.ModelAdmin):
    list_display = ['result_n', 'content']


admin.site.register(models.MbtiText, MTextAdmin)

admin.site.register(models.Result)
