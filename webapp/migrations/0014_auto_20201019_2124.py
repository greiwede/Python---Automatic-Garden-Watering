# Generated by Django 3.1 on 2020-10-19 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20201019_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherdata',
            name='location_id',
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='location_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.location'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='owm_id',
            field=models.IntegerField(),
        ),
    ]
