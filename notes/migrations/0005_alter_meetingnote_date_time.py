# Generated by Django 3.2.3 on 2021-07-18 05:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_trash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingnote',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 18, 5, 14, 48, 30506, tzinfo=utc)),
        ),
    ]
