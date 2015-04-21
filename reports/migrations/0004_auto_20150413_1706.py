# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20150413_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pediatrician',
            field=models.CharField(default='na', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='pediatrician_phone',
            field=models.CharField(default='na', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='referral_physician',
            field=models.CharField(default='na', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='rererral_physician_fax',
            field=models.CharField(default='na', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='rererral_physician_phone',
            field=models.CharField(default='na', max_length=20),
            preserve_default=False,
        ),
    ]
