# Generated by Django 2.2.2 on 2019-07-29 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='name',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
