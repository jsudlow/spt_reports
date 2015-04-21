# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_speechevaluationreport_identifying_information_and_referral'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='injury',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='surgery',
            name='patient',
        ),
        migrations.DeleteModel(
            name='Injury',
        ),
        migrations.DeleteModel(
            name='Surgery',
        ),
    ]
