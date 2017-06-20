# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgprofile', '0008_chapterinvite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterinvite',
            name='TOKEN',
            field=models.CharField(max_length=112, null=True),
        ),
    ]
