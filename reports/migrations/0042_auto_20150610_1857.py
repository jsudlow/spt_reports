# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0041_auto_20150610_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='adjusted_age',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
