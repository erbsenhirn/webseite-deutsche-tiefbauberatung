# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-13 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins', '0008_mappluginmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappluginmodel',
            name='karte_bild',
            field=models.FileField(upload_to='map-images/'),
        ),
        migrations.AlterField(
            model_name='mappluginmodel',
            name='legende_bild',
            field=models.FileField(upload_to='map-images/'),
        ),
    ]