# Generated by Django 4.2 on 2023-06-11 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mins',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='post',
            name='ratings',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='post',
            name='year',
            field=models.CharField(default='', max_length=4),
        ),
    ]