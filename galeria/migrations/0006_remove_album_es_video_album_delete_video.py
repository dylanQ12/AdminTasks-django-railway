# Generated by Django 5.0.6 on 2024-05-17 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_video_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='es_video_album',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
