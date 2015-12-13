# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0049_auto_20151213_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='activities_of_daily_living',
            field=ckeditor.fields.RichTextField(default='activities of daily living'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='adaptive_skills',
            field=ckeditor.fields.RichTextField(default='adaptive skills'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='clinical_impressions_and_recommendations',
            field=ckeditor.fields.RichTextField(default='clinical impressions and recommendaions'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='education',
            field=ckeditor.fields.RichTextField(default='education'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='electronic_signature',
            field=ckeditor.fields.RichTextField(default='electronic sig'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='fine_motor_skills',
            field=ckeditor.fields.RichTextField(default='fine motor skills'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='long_term_goals',
            field=ckeditor.fields.RichTextField(default='long term goals'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='muscle_tone',
            field=ckeditor.fields.RichTextField(default='muscle tone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='referrals_and_follow_up',
            field=ckeditor.fields.RichTextField(default='referrals and follow up'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='sensory_processing',
            field=ckeditor.fields.RichTextField(default='sensory processing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='short_term_goals',
            field=ckeditor.fields.RichTextField(default='short term goals'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='statement_of_medical_neccessity',
            field=ckeditor.fields.RichTextField(default='statement of medical neccessity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='strength',
            field=ckeditor.fields.RichTextField(default='strength'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='visual_motor_skills',
            field=ckeditor.fields.RichTextField(default='visual motor skills'),
            preserve_default=False,
        ),
    ]
