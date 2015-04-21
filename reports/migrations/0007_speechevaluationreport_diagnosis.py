# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20150413_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechevaluationreport',
            name='diagnosis',
            field=models.CharField(default='Apraxia', max_length=200),
            preserve_default=False,
        ),
    ]
