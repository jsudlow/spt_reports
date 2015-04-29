# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0036_auto_20150427_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='payor',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='pol_claim_number',
        ),
    ]
