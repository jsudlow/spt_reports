# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0025_speechevaluationreport_developmental'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speechevaluationreport',
            old_name='medical_history',
            new_name='medical',
        ),
    ]
