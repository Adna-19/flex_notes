# Generated by Django 3.2.3 on 2021-08-23 12:38

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0014_sharednote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essayoutline',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='essayoutline',
            name='conclusion',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='essayoutline',
            name='introduction',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='meetingnote',
            name='notes',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
