# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0037_auto_20150427_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='account_number',
        ),
    ]
