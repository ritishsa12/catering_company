# Generated by Django 4.2.2 on 2023-11-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_images_image12'),
    ]

    operations = [
        migrations.CreateModel(
            name='email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
