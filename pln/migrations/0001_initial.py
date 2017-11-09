# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', unique=True, max_length=254)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
                ('description', models.TextField(null=True, blank=True)),
                ('icon', models.URLField(max_length=254, null=True, blank=True)),
                ('privacy', models.CharField(max_length=254, null=True, blank=True)),
                ('tutorial', models.CharField(max_length=254, null=True, blank=True)),
                ('url', models.CharField(max_length=254, null=True, blank=True)),
                ('testimonial', models.CharField(max_length=255, null=True, blank=True)),
                ('is_avaiable', models.BooleanField(default=True, choices=[(True, 'Yes'), (False, 'No')])),
            ],
        ),
        migrations.CreateModel(
            name='AppFormat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='AppFunction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='AppPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='AppSupport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='AppType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='app',
            name='format',
            field=models.ManyToManyField(to='pln.AppFormat'),
        ),
        migrations.AddField(
            model_name='app',
            name='function',
            field=models.ManyToManyField(to='pln.AppFunction'),
        ),
        migrations.AddField(
            model_name='app',
            name='icon_image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.Image', null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='price',
            field=models.ManyToManyField(to='pln.AppPrice'),
        ),
        migrations.AddField(
            model_name='app',
            name='support',
            field=models.ManyToManyField(to='pln.AppSupport'),
        ),
        migrations.AddField(
            model_name='app',
            name='type',
            field=models.ManyToManyField(to='pln.AppType'),
        ),
    ]
