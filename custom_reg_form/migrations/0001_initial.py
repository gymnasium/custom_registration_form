# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):
    
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID',
                )),
                ('market', models.CharField(
                    choices=[
                        (b'Not Applicable', b'NA'),
                        (b'Boston', b'10'),
                    ],
                    max_length=5,
                    verbose_name=b'Select Nearest Aquent Office',
                )),
                ('receive_job_offers', models.BooleanField(
                    default=False,
                    editable=True,
                    verbose_name=b'Receive emails with job opportunities?',
                )),
                ('user', models.OneToOneField(
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL,
                )),
            ],
        ),
    ]
