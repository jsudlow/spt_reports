# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0065_auto_20160414_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechevaluationreport',
            name='clinician',
            field=models.CharField(default='fill in', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='supervising_clinician',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
