# Generated by Django 3.2.3 on 2021-08-21 13:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0011_auto_20210820_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingnote',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 21, 13, 33, 13, 335401, tzinfo=utc)),
        ),
    ]