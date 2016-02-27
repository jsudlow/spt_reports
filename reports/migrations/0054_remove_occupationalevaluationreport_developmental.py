# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0053_auto_20160224_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occupationalevaluationreport',
            name='developmental',
        ),
    ]
