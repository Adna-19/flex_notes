# Generated by Django 3.2.3 on 2021-08-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='claps',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]