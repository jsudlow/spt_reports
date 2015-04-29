# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0031_auto_20150427_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='articulation',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
