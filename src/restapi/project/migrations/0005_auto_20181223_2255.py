# Generated by Django 2.1.2 on 2018-12-23 17:25

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181213_2117'),
        ('project', '0004_auto_20181223_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_replies', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=25), default=list, size=None)),
                ('comment_text', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('previous_edits', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2018, 12, 23, 22, 55, 49, 809891))),
                ('commenter', models.ForeignKey(db_column='commenter', on_delete=django.db.models.deletion.DO_NOTHING, to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='IssueReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_text', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('previous_edits', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2018, 12, 23, 22, 55, 49, 811111))),
                ('comment_id', models.ForeignKey(db_column='comment_id', on_delete=django.db.models.deletion.CASCADE, to='project.IssueComment')),
                ('respondent', models.ForeignKey(db_column='respondent', on_delete=django.db.models.deletion.DO_NOTHING, to='users.User')),
            ],
        ),
        migrations.AlterField(
            model_name='issue',
            name='comments',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='issue',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 23, 22, 55, 49, 809102)),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 23, 22, 55, 49, 808095)),
        ),
        migrations.AlterField(
            model_name='project',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 23, 22, 55, 49, 808252)),
        ),
        migrations.AddField(
            model_name='issuecomment',
            name='issue_id',
            field=models.ForeignKey(db_column='issue_id', on_delete=django.db.models.deletion.DO_NOTHING, to='project.Issue'),
        ),
        migrations.AddField(
            model_name='issuecomment',
            name='project_id',
            field=models.ForeignKey(db_column='project_id', on_delete=django.db.models.deletion.DO_NOTHING, to='project.Project'),
        ),
    ]