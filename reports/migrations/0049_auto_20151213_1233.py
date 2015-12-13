# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0048_auto_20151110_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='background_information',
            field=ckeditor.fields.RichTextField(default='back'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='developmental',
            field=ckeditor.fields.RichTextField(default='developmental'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='diagnosis',
            field=models.CharField(default='diagnosis', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='family_social',
            field=ckeditor.fields.RichTextField(default='familysocial'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='identifying_information_and_referral',
            field=ckeditor.fields.RichTextField(default='identifyinginofr and referal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='medical',
            field=ckeditor.fields.RichTextField(default='medical'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='parent_concern',
            field=ckeditor.fields.RichTextField(default='parent concern'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalevaluationreport',
            name='pregnancy_and_birth',
            field=ckeditor.fields.RichTextField(default='pregnancy and birth'),
            preserve_default=False,
        ),
    ]
