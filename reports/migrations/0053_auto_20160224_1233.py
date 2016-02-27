# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0052_remove_occupationalevaluationreport_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupationalevaluationreport',
            name='pregnancy_and_birth',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
