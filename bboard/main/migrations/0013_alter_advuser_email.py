# Generated by Django 4.0.6 on 2022-08-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_advuser_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Адрес электронной почты'),
        ),
    ]
