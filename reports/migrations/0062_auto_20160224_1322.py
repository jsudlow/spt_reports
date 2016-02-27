# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0061_auto_20160224_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupationalevaluationreport',
            name='sensory_processing',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
