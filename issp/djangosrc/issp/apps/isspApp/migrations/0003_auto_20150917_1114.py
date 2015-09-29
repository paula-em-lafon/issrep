# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isspApp', '0002_auto_20150917_1025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='fullname',
            new_name='full_name',
        ),
    ]
