# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0014_test_testscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechevaluationreport',
            name='test',
            field=models.ForeignKey(default=1, to='reports.Test'),
            preserve_default=False,
        ),
    ]
