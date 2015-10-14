# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0046_occupationalevaluationreport_date_of_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='location',
            field=models.CharField(default='SPT NORTH', max_length=200, choices=[(b'Aurora', b'Aurora'), (b'Naperville North', b'Naperville North'), (b'Naperville Central', b'Naperville Central')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='report_type',
            field=models.CharField(default='otreport', max_length=200, choices=[(b'Initial Speech-Language Evaluation Report', b'Initial Speech-Language Evaluation Report'), (b'Speech-Language Re-evaluation Report', b'Speech-Language Re-evaluation Report')]),
            preserve_default=False,
        ),
    ]
