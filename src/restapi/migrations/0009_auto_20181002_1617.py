# Generated by Django 2.0.7 on 2018-10-02 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0008_auto_20181002_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 2, 16, 17, 52, 509601)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 2, 16, 17, 52, 509072)),
        ),
    ]
