# Generated by Django 3.2.8 on 2022-06-07 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_user_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_pic',
        ),
    ]
