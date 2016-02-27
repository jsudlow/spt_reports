# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0050_auto_20151213_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occupationalevaluationreport',
            name='muscle_tone',
        ),
    ]
