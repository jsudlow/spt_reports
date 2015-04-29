# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0034_speechevaluationreport_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechevaluationreport',
            name='report_type',
            field=models.CharField(default='Speech Eval', max_length=200, choices=[(b'Initial Speech-Language Evaluation Report', b'Initial Speech-Language Evaluation Report,'), (b'Speech-Language Re-evaluation Report', b'Speech-Language Re-evaluation Report')]),
            preserve_default=False,
        ),
    ]
