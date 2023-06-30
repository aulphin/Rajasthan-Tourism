# Generated by Django 2.2.2 on 2019-07-30 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_booked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.TextField()),
                ('todate', models.DateField()),
                ('enddate', models.DateField()),
                ('days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Locations')),
            ],
        ),
        migrations.CreateModel(
            name='Packagelocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Locations')),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Booked',
        ),
        migrations.AddField(
            model_name='packagelocation',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Packages'),
        ),
        migrations.AddField(
            model_name='booking',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Packages'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Register'),
        ),
    ]
