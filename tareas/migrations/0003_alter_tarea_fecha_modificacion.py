# Generated by Django 5.0.6 on 2024-05-15 00:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_tarea_fecha_modificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
