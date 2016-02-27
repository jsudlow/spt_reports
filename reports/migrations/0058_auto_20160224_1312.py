# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0057_remove_occupationalevaluationreport_family_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupationalevaluationreport',
            name='visual_motor_skills',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
