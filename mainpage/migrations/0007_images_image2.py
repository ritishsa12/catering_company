# Generated by Django 4.2.2 on 2023-11-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_images_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image2',
            field=models.ImageField(default=1, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
