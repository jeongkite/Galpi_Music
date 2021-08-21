from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Mbti(models.Model):
    e_i = models.IntegerField(default=0, verbose_name="E/I")
    s_n = models.IntegerField(default=0, verbose_name="S/N")
    t_f = models.IntegerField(default=0, verbose_name="T/F")
    p_j = models.IntegerField(default=0, verbose_name="P/J")

    def __str__(self):
        return self.kind


class Answer(models.Model):
    a_text = models.TextField(verbose_name="답변 텍스트")

    def __str__(self):
        return self.a_text


class Question(models.Model):
    q_number = models.IntegerField(verbose_name="No.")
    q_title = models.TextField(verbose_name="질문")
    answer = models.ForeignKey(
        'Answer', on_delete=models.SET_NULL, null=True, verbose_name="답변")


class MbtiText(models.Model):
    content = models.TextField(verbose_name="mbti 세부 텍스트")


class Result(models.Model):
    mbti = models.CharField(max_length=4, verbose_name="mbti 유형")
    song = models.TextField(verbose_name="노래 제목")
    singer = models.TextField(verbose_name="가수")
    close_line = models.TextField(verbose_name="마무리 멘트")
    description = models.TextField(verbose_name="장면 묘사")
    feature = models.ForeignKey(
        'MbtiText', on_delete=models.SET_NULL, null=True, verbose_name="mbti 특징")
    heart = models.TextField(verbose_name="속마음")
    partner = models.OneToOneField(
        'self', on_delete=models.SET_NULL, null=True, verbose_name="결이 같은 사람")
