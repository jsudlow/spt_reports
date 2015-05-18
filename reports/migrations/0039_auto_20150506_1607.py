# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0038_remove_patient_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='location',
            field=models.CharField(max_length=200, choices=[(b'Aurora', b'Aurora'), (b'Naperville North', b'Naperville North'), (b'Naperville Central', b'Naperville Central')]),
        ),
    ]
