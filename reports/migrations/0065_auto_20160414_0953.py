# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0064_occupationalevaluationreport_supervising_clinician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupationalevaluationreport',
            name='referrals_and_follow_up',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
