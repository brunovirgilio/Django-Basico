# Generated by Django 3.1.5 on 2021-02-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbasico', '0004_auto_20210205_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='sulamericana',
            field=models.CharField(default='', max_length=3),
        ),
    ]
