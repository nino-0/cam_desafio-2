# Generated by Django 4.2 on 2023-04-21 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_rename_nome_deparment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deparment',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]