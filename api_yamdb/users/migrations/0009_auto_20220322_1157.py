# Generated by Django 3.2.12 on 2022-03-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.TextField(default='000000'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.TextField(choices=[('user', 'User'), ('moderator', 'Moderator'), ('admin', 'Admin')], default='user'),
        ),
    ]
