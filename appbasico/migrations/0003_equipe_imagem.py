# Generated by Django 3.1.2 on 2021-02-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbasico', '0002_auto_20210126_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='appbasico'),
        ),
    ]
