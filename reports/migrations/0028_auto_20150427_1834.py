# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0027_speechevaluationreport_electronic_signature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speechevaluationreport',
            old_name='language_evaluation',
            new_name='initial_language_evaluation',
        ),
    ]
