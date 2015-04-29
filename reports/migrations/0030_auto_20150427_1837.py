# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0029_speechevaluationreport_speech_language_reevaluation_and_progress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speechevaluationreport',
            old_name='summary_and_recommendations',
            new_name='clinical_impressions_and_recommendations',
        ),
    ]
