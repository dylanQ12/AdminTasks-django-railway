# Generated by Django 5.0.6 on 2024-05-13 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.URLField(max_length=390, null=True),
        ),
    ]
