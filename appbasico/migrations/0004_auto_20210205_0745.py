# Generated by Django 3.1.5 on 2021-02-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbasico', '0003_equipe_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='imagem',
            field=models.ImageField(upload_to='media'),
        ),
    ]
