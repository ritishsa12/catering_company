# Generated by Django 4.2.2 on 2023-11-10 06:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0016_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
