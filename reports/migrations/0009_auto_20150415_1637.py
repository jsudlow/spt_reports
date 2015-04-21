# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20150415_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='communication_concern',
            field=tinymce.models.HTMLField(),
        ),
    ]
