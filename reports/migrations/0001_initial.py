# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Injury',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('injury_date', models.DateField()),
                ('injury_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('account_number', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('clinician', models.CharField(max_length=30)),
                ('supervising_clinician', models.CharField(max_length=30)),
                ('payor', models.CharField(max_length=30)),
                ('pol_claim_number', models.CharField(max_length=30)),
                ('ssn', models.CharField(max_length=20)),
                ('visits', models.IntegerField()),
                ('chronological_age', models.IntegerField()),
                ('adjusted_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('doctor_type', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('fax', models.CharField(max_length=30)),
                ('patient', models.ForeignKey(to='reports.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='SpeechEvaluationReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_visit', models.DateField()),
                ('patient', models.ForeignKey(to='reports.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('surgery_date', models.DateField()),
                ('surgery_description', models.TextField()),
                ('patient', models.ForeignKey(to='reports.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='injury',
            name='patient',
            field=models.ForeignKey(to='reports.Patient'),
        ),
    ]
