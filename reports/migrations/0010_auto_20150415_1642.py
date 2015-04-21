# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_auto_20150415_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='pregnancy_and_birth',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
