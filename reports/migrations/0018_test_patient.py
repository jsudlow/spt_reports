# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0017_remove_test_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='patient',
            field=models.ForeignKey(default='1', to='reports.Patient'),
            preserve_default=False,
        ),
    ]
