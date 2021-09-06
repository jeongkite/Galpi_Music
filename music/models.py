from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Mbti(models.Model):
    hash_code = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(default=1, verbose_name="진행도")
    e_i = models.IntegerField(default=0, verbose_name="E/I")
    s_n = models.IntegerField(default=0, verbose_name="S/N")
    t_f = models.IntegerField(default=0, verbose_name="T/F")
    p_j = models.IntegerField(default=0, verbose_name="P/J")


class Answer(models.Model):
    a_type = models.CharField(max_length=1, verbose_name="답변 유형")
    a_text = models.TextField(verbose_name="답변 텍스트")
    question_n = models.ForeignKey(
        'Question', on_delete=models.SET_NULL, null=True, verbose_name="매칭 질문")

    def __str__(self):
        return self.a_text


class Question(models.Model):
    q_number = models.IntegerField(verbose_name="No.")
    q_title = models.TextField(verbose_name="질문")


class MbtiText(models.Model):
    content = models.TextField(verbose_name="mbti 세부 텍스트")
    result_n = models.ForeignKey(
        'Result', on_delete=models.SET_NULL, null=True, verbose_name="매칭 결과")


class Result(models.Model):
    mbti = models.CharField(max_length=4, verbose_name="mbti 유형")
    song = models.TextField(verbose_name="노래 제목")
    singer = models.TextField(verbose_name="가수")
    close_line = models.TextField(verbose_name="마무리 멘트")
    description = models.TextField(verbose_name="장면 묘사")
    heart = models.TextField(verbose_name="속마음")
    partner = models.OneToOneField(
        'self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="결이 같은 사람")
    partner_text = models.TextField(null=True, verbose_name="파트너 텍스트")

    def __str__(self):
        return self.mbti
