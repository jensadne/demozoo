# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-19 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parties', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(db_index=True, max_length=255)),
                ('is_deleted', models.BooleanField(default=False)),
                ('first_seen_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_seen_at', models.DateTimeField()),
                ('last_spidered_at', models.DateTimeField(blank=True, null=True)),
                ('competitions', models.ManyToManyField(related_name='sceneorg_directories', to='parties.Competition')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subdirectories', to='sceneorg.Directory')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(db_index=True, max_length=255)),
                ('is_deleted', models.BooleanField(default=False)),
                ('first_seen_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_seen_at', models.DateTimeField()),
                ('size', models.BigIntegerField(null=True)),
                ('directory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='sceneorg.Directory')),
            ],
        ),
    ]
