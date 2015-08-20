# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0042_auto_20150610_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speechevaluationreport',
            old_name='initial_language_evaluation',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='speechevaluationreport',
            old_name='speech_language_reevaluation_and_progress',
            new_name='speech_language_progress',
        ),
    ]
