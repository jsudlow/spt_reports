# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0030_auto_20150427_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechevaluationreport',
            name='long_term_goals',
            field=ckeditor.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='referrals_and_follow_up',
            field=ckeditor.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='short_term_goals',
            field=ckeditor.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speechevaluationreport',
            name='statement_of_medical_neccessity',
            field=ckeditor.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
    ]
