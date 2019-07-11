# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-06 20:13
from __future__ import unicode_literals

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoscene', '0008_add_releaser_admin_search_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='releaser',
            name='admin_search_document',
            field=django.contrib.postgres.search.SearchVectorField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='releaser',
            name='search_document',
            field=django.contrib.postgres.search.SearchVectorField(editable=False, null=True),
        ),
    ]