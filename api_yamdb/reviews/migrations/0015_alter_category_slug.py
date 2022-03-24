# Generated by Django 3.2.12 on 2022-03-24 07:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_auto_20220322_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(message='Slug должен состоять из набора латинских букв и цифр', regex='^[-a-zA-Z0-9_]+$')]),
        ),
    ]
