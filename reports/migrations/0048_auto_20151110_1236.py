# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0047_auto_20151013_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupationalevaluationreport',
            name='report_type',
            field=models.CharField(max_length=200, choices=[(b'Initial Occupational-Language Evaluation Report', b'Initial Occupational-Language Evaluation Report'), (b'Occupational-Language Re-evaluation Report', b'Occupational-Language Re-evaluation Report')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='chronological_age',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
    ]
