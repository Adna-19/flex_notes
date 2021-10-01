# Generated by Django 3.2.3 on 2021-08-16 12:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_auto_20210802_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='notetype',
            name='icon_class',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='meetingnote',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 16, 12, 54, 41, 582415, tzinfo=utc)),
        ),
    ]
