# Generated by Django 3.1 on 2020-10-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0024_auto_20201025_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='valve',
            name='activate_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
