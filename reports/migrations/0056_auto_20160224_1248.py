# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0055_auto_20160224_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupationalevaluationreport',
            name='medical_and_developmental',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
