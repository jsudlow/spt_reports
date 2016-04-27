# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0063_occupationalevaluationreport_clinician'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='supervising_clinician',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
