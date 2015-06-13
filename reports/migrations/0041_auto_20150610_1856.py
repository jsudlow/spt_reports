# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0040_auto_20150610_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='chronological_age',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
