# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechevaluationreport',
            name='identifying_information_and_referral',
            field=models.TextField(default=b''),
        ),
    ]
