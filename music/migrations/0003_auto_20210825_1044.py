# Generated by Django 3.2.6 on 2021-08-25 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20210825_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='question_n',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.question', verbose_name='매칭 질문'),
        ),
        migrations.AddField(
            model_name='mbtitext',
            name='result_n',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.result', verbose_name='매칭 결과'),
        ),
    ]
