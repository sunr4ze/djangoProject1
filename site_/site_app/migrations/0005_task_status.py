# Generated by Django 4.1.4 on 2023-01-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0004_task_deadline_task_priority_task_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='', max_length=40, verbose_name='Статус'),
            preserve_default=False,
        ),
    ]
