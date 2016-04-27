# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0066_auto_20160425_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='clinician',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='supervising_clinician',
        ),
    ]
