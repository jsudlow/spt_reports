# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0033_auto_20150427_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechevaluationreport',
            name='location',
            field=models.CharField(default='Aurora', max_length=200, choices=[(b'Aurora', b'Aurora'), (b'Naperville North', b'Naperville North'), (b'Napervile Central', b'Naperville Central')]),
            preserve_default=False,
        ),
    ]
