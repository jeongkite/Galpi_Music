# Generated by Django 3.2.6 on 2021-08-25 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20210825_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='feature',
        ),
    ]
