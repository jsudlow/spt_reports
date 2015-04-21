# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0020_auto_20150420_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speechevaluationreport',
            name='newborn_hearing_screening',
        ),
    ]
