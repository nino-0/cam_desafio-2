# Generated by Django 4.2 on 2023-04-21 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deparment',
            old_name='nome',
            new_name='name',
        ),
    ]
