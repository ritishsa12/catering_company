# Generated by Django 4.2.2 on 2023-11-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0019_product_image1_product_image2_product_image3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image13',
            field=models.ImageField(default=1, upload_to='gallery'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='image14',
            field=models.ImageField(default=1, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
