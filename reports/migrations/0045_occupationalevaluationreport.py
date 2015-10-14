# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0044_speechevaluationreport_behavioral_observation'),
    ]

    operations = [
        migrations.CreateModel(
            name='OccupationalEvaluationReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('patient', models.ForeignKey(to='reports.Patient')),
            ],
        ),
    ]
