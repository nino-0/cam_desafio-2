# Generated by Django 4.2 on 2023-04-21 01:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0003_alter_deparment_name'),
        ('employee', '0002_alter_employee_cpf_alter_employee_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('total_hours_to_complete', models.FloatField(default=0)),
                ('total_hours_completed', models.FloatField(default=0)),
                ('estimated_date', models.DateField()),
                ('last_measurement', models.DateField(default=datetime.date.today)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.deparment')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workload', models.FloatField(default=0)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('project_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
    ]
