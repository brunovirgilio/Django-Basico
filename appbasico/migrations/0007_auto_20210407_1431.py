# Generated by Django 3.1.7 on 2021-04-07 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasico', '0006_postagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postagem',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='postagem',
            name='criado',
        ),
        migrations.RemoveField(
            model_name='postagem',
            name='modificado',
        ),
    ]
