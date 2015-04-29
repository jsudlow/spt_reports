# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0028_auto_20150427_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechevaluationreport',
            name='speech_language_reevaluation_and_progress',
            field=ckeditor.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
    ]
