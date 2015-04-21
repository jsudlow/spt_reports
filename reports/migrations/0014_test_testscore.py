# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0013_auto_20150415_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TestScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score_text', models.CharField(max_length=200)),
                ('score_value', models.CharField(max_length=20)),
                ('test', models.ForeignKey(to='reports.Test')),
            ],
        ),
    ]
