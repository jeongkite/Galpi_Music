from django.db import models
from django.db.models.fields import TextField

# Create your models here.


class Mbti(models.Model):
    e_i = models.IntegerField()
    s_n = models.IntegerField()
    t_f = models.IntegerField()
    p_j = models.IntegerField()

    def __str__(self):
        return self.kind


class Answer(models.Model):
    a_text = models.TextField(verbose_name="")

    def __str__(self):
        return self.a_text


class Question(models.Model):
    q_number = models.IntegerField(verbose_name="")
    q_title = models.TextField(verbose_name="")
    answer = models.ForeignKey(to=Answer, verbose_name="")


class Result(models.Model):
    mbti = models.CharField(max_length=4, verbose_name="")
    song = models.TextField(verbose_name="")
    singer = models.TextField(verbose_name="")
    close_line = models.TextField(verbose_name="")
    description = models.TextField(verbose_name="")
