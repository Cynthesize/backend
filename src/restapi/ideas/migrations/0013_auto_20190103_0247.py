# Generated by Django 2.1.2 on 2019-01-02 21:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0012_auto_20181223_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 3, 2, 47, 45, 33646)),
        ),
    ]
