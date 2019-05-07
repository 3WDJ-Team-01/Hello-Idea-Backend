# Generated by Django 2.1.5 on 2019-04-24 01:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190423_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_intro',
            field=models.CharField(default='Hello', max_length=50),
        ),
        migrations.AlterField(
            model_name='idea',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 24, 1, 47, 50, 604779, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 24, 1, 47, 50, 603783, tzinfo=utc)),
        ),
    ]