# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateTimeField(verbose_name=b'date of birth')),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
