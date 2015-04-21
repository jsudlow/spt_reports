# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0021_remove_speechevaluationreport_newborn_hearing_screening'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speechevaluationreport',
            old_name='social_family',
            new_name='family_social',
        ),
    ]
