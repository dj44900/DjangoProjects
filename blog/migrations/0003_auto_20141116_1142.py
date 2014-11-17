# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='vidurl',
            new_name='embedid',
        ),
    ]
