# Generated by Django 4.0.6 on 2022-08-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_advuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
