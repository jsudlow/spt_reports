# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0068_auto_20160427_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='hearing',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
