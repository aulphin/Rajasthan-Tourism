# Generated by Django 2.2.2 on 2019-07-30 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_cities_locations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.IntegerField()),
                ('todate', models.DateField()),
                ('fromdate', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
