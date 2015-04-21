# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0022_auto_20150420_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speechevaluationreport',
            old_name='evaluation',
            new_name='articulation',
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='cranial_nerve_exam',
            field=ckeditor.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='hearing',
            field=ckeditor.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='language_evaluation',
            field=ckeditor.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='language_sample',
            field=ckeditor.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='summary_and_recommendations',
            field=ckeditor.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='voice_and_fluency',
            field=ckeditor.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
    ]
