# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0067_auto_20160425_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='cranial_nerve_exam',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='developmental',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='education',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='family_social',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='medical',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='pregnancy_and_birth',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='short_term_goals',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
