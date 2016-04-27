# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0062_auto_20160224_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='clinician',
            field=models.CharField(default='Fill In Name', max_length=30),
            preserve_default=False,
        ),
    ]
