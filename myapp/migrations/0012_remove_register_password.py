# Generated by Django 2.2.2 on 2019-07-29 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20190729_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='password',
        ),
    ]
