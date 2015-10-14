# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0045_occupationalevaluationreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='date_of_visit',
            field=models.DateField(default='2005-09-01'),
            preserve_default=False,
        ),
    ]
