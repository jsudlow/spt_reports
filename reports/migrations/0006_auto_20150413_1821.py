# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_patient_pediatrician_fax'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='rererral_physician_fax',
            new_name='referral_physician_fax',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='rererral_physician_phone',
            new_name='referral_physician_phone',
        ),
    ]
