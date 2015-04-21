# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_speechevaluationreport_diagnosis'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechevaluationreport',
            name='communication_concern',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='education',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='evaluation',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='medical_history',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='newborn_hearing_screening',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='pregnancy_and_birth',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='social_family',
            field=models.TextField(default=b''),
        ),
    ]
