# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20150413_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pediatrician_fax',
            field=models.CharField(default='na', max_length=20),
            preserve_default=False,
        ),
    ]
