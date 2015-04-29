# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0032_auto_20150427_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='initial_language_evaluation',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='language_sample',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='speech_language_reevaluation_and_progress',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
