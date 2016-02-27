# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0051_remove_occupationalevaluationreport_muscle_tone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occupationalevaluationreport',
            name='education',
        ),
    ]
