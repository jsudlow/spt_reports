# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0024_speechevaluationreport_background_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechevaluationreport',
            name='developmental',
            field=ckeditor.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
    ]
