# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgprofile', '0009_auto_20170611_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapterinvite',
            old_name='INVITE_DATETIME',
            new_name='EXPIRY_DATETIME',
        ),
    ]
