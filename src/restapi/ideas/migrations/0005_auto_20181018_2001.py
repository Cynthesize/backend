# Generated by Django 2.0.7 on 2018-10-18 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_auto_20181018_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 20, 1, 6, 871670)),
        ),
    ]
