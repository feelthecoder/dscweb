# Generated by Django 3.1 on 2020-10-13 14:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
