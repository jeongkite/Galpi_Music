# Generated by Django 3.2.6 on 2021-08-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_result_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='mbti',
            name='order',
            field=models.IntegerField(default=1, verbose_name='진행도'),
        ),
    ]