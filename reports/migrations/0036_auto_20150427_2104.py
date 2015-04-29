# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0035_speechevaluationreport_report_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='ssn',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='visits',
        ),
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='report_type',
            field=models.CharField(max_length=200, choices=[(b'Initial Speech-Language Evaluation Report', b'Initial Speech-Language Evaluation Report'), (b'Speech-Language Re-evaluation Report', b'Speech-Language Re-evaluation Report')]),
        ),
    ]
