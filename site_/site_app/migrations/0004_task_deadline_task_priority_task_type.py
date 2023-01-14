# Generated by Django 4.1.4 on 2023-01-14 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0003_remove_task_type_task_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.CharField(default='', max_length=40, verbose_name='Сроки выполнения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(default='', max_length=40, verbose_name='Приоритет'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.CharField(default='', max_length=40, verbose_name='Тип'),
            preserve_default=False,
        ),
    ]
