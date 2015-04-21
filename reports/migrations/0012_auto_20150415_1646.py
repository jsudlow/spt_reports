# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_auto_20150415_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='communication_concern',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
