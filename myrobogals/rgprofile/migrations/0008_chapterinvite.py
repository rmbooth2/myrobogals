# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgprofile', '0007_user_code_of_conduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChapterInvite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=64)),
                ('staff_access', models.NullBooleanField()),
                ('superuser_access', models.NullBooleanField()),
                ('INVITE_DATETIME', models.DateTimeField(null=True)),
                ('TOKEN', models.IntegerField(null=True)),
                ('CHAPTER_URL', models.CharField(max_length=80)),
            ],
        ),
    ]
