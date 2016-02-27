# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0054_remove_occupationalevaluationreport_developmental'),
    ]

    operations = [
        migrations.RenameField(
            model_name='occupationalevaluationreport',
            old_name='medical',
            new_name='medical_and_developmental',
        ),
    ]
