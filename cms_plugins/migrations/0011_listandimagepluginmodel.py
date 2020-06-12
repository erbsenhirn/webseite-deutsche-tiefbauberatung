# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-13 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('cms_plugins', '0010_auto_20200513_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListAndImagePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_listandimagepluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('ueberschrift', models.CharField(max_length=128)),
                ('bild', models.FileField(upload_to='list-images/')),
                ('stichkpunkt_1', models.CharField(blank=True, max_length=1024)),
                ('stichkpunkt_2', models.CharField(blank=True, max_length=1024)),
                ('stichkpunkt_3', models.CharField(blank=True, max_length=1024)),
                ('stichkpunkt_4', models.CharField(blank=True, max_length=1024)),
                ('stichkpunkt_5', models.CharField(blank=True, max_length=1024)),
                ('stichkpunkt_6', models.CharField(blank=True, max_length=1024)),
                ('stichkpunkt_7', models.CharField(blank=True, max_length=1024)),
                ('stichkpunkt_8', models.CharField(blank=True, max_length=1024)),
                ('stichkpunkt_9', models.CharField(blank=True, max_length=1024)),
                ('stichkpunkt_10', models.CharField(blank=True, max_length=1024)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]