# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0026_auto_20150420_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechevaluationreport',
            name='electronic_signature',
            field=ckeditor.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
    ]
