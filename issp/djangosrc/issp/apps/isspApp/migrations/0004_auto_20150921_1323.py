# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isspApp', '0003_auto_20150917_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedSensor',
            fields=[
                ('id_assigned_sensor', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id_card', models.AutoField(serialize=False, primary_key=True)),
                ('card_serial', models.CharField(max_length=6, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PositionInCard',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('id_position_in_card', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RackDetails',
            fields=[
                ('id_Rack', models.AutoField(serialize=False, primary_key=True)),
                ('rack_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id_reading', models.AutoField(serialize=False, primary_key=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('data', models.CharField(max_length=20)),
                ('assigned_sensor', models.ForeignKey(to='isspApp.AssignedSensor')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id_Version', models.AutoField(serialize=False, primary_key=True)),
                ('type_card', models.CharField(max_length=20)),
                ('version_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Warnings',
            fields=[
                ('id_warning', models.AutoField(serialize=False, primary_key=True)),
                ('reading', models.ForeignKey(to='isspApp.Reading')),
            ],
        ),
        migrations.CreateModel(
            name='WarningTypes',
            fields=[
                ('id_warning_type', models.AutoField(serialize=False, primary_key=True)),
                ('warning_name', models.CharField(max_length=30)),
                ('description_warning', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='warnings',
            name='warning_types',
            field=models.ForeignKey(to='isspApp.WarningTypes'),
        ),
        migrations.AddField(
            model_name='card',
            name='rack_detail',
            field=models.ForeignKey(to='isspApp.RackDetails'),
        ),
        migrations.AddField(
            model_name='assignedsensor',
            name='cardId',
            field=models.ForeignKey(to='isspApp.Card'),
        ),
        migrations.AddField(
            model_name='assignedsensor',
            name='position_within_card',
            field=models.ForeignKey(to='isspApp.PositionInCard'),
        ),
    ]
