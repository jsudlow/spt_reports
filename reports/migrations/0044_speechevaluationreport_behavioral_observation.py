# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0043_auto_20150806_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechevaluationreport',
            name='behavioral_observation',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
