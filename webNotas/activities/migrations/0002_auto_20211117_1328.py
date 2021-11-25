# Generated by Django 3.2.8 on 2021-11-17 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='activities/news/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='fichero',
            field=models.FileField(blank=True, null=True, upload_to='activities/videos/', verbose_name='Fichero'),
        ),
    ]
