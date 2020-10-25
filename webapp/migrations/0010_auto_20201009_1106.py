# Generated by Django 3.1.1 on 2020-10-09 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20201008_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='pump',
            field=models.ManyToManyField(to='webapp.Pump'),
        ),
        migrations.AddField(
            model_name='plan',
            name='sensor',
            field=models.ManyToManyField(to='webapp.Sensor'),
        ),
        migrations.AddField(
            model_name='plan',
            name='sprinkler',
            field=models.ManyToManyField(to='webapp.Sprinkler'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='allow_time_start',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='allow_time_stop',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='deny_time_start',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='deny_time_stop',
            field=models.TimeField(),
        ),
    ]
