# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0012_auto_20150415_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='education',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='evaluation',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='medical_history',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='newborn_hearing_screening',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='social_family',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
