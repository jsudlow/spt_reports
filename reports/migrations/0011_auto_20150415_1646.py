# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_auto_20150415_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechevaluationreport',
            name='identifying_information_and_referral',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
