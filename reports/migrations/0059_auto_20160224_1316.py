# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0058_auto_20160224_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='occupationalevaluationreport',
            old_name='adaptive_skills',
            new_name='handwriting',
        ),
    ]
