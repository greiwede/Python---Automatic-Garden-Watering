# Generated by Django 3.1 on 2020-10-25 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0025_valve_activate_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wateringstatistic',
            name='valve_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.valve'),
        ),
    ]
