# Generated by Django 4.0.6 on 2022-08-03 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_advuser_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advuser',
            name='image',
        ),
    ]
