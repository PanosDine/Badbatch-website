# Generated by Django 3.1.5 on 2021-01-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0007_auto_20210120_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='url',
            field=models.URLField(),
        ),
    ]