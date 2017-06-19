# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pic_cms.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cid', models.CharField(max_length=100)),
                ('cname', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['cid'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pid', models.CharField(max_length=100)),
                ('image', pic_cms.fields.ThumbnailImageField(upload_to=b'photos')),
                ('is_checked', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xba\xba\xe5\xb7\xa5\xe6\xa0\xa1\xe9\xaa\x8c')),
                ('is_valid', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe6\x95\x88\xe5\x9b\xbe\xe7\x89\x87')),
                ('ocr_text', models.CharField(max_length=300, verbose_name=b'OCR\xe6\x96\x87\xe6\x9c\xac', blank=True)),
                ('correct_text', models.CharField(max_length=300, verbose_name=b'\xe7\xb2\xbe\xe5\x87\x86\xe6\x96\x87\xe6\x9c\xac', blank=True)),
                ('get_result', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\xad\xa3\xe7\xa1\xae\xe7\xbb\x93\xe6\x9e\x9c')),
                ('same_pid', models.CharField(max_length=300, verbose_name=b'\xe7\x9b\xb8\xe5\x90\x8c\xe9\xa2\x98\xe7\x9b\xaeid', blank=True)),
                ('err_source', models.CharField(max_length=300, verbose_name=b'\xe9\x94\x99\xe8\xaf\xaf\xe5\x8e\x9f\xe5\x9b\xa0', blank=True)),
                ('course', models.ForeignKey(to='pic_app.Course')),
            ],
        ),
    ]
