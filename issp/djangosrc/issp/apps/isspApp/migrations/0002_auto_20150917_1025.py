# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isspApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='fullname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
