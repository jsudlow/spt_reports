# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0019_remove_speechevaluationreport_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speechevaluationreport',
            old_name='communication_concern',
            new_name='parent_concern',
        ),
    ]
