# Generated by Django 3.2.3 on 2021-07-26 07:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0005_alter_meetingnote_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blanknote',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='blanknote',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='essayoutline',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='essayoutline',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='lecturenote',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='lecturenote',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='mealplanner',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='mealplanner',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='meetingnote',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='meetingnote',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='projectplan',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='projectplan',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='todonote',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='todonote',
            name='date_updated',
        ),
        migrations.AddField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 7, 26, 7, 30, 9, 644544, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='meetingnote',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 26, 7, 28, 58, 850643, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='StickyNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sticky_notes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]