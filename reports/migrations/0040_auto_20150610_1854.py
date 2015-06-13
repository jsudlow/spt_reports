# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0039_auto_20150506_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='adjusted_age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='chronological_age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pediatrician',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pediatrician_fax',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pediatrician_phone',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='supervising_clinician',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
