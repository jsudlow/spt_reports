# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0059_auto_20160224_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupationalevaluationreport',
            name='handwriting',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
