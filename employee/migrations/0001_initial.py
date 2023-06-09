# Generated by Django 4.2 on 2023-04-21 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0002_rename_nome_deparment_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=13)),
                ('gender', models.CharField(max_length=1)),
                ('has_a_license', models.BooleanField(default=False)),
                ('wage_value', models.FloatField(default=0)),
                ('weekly_workload', models.FloatField(default=0)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.deparment')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
