# Generated by Django 3.1.7 on 2021-04-12 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasico', '0008_auto_20210409_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postagem',
            name='slug',
        ),
    ]
