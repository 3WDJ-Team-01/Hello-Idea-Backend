# Generated by Django 2.1.5 on 2019-05-02 03:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20190502_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 3, 46, 41, 459099, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 3, 46, 41, 458103, tzinfo=utc)),
        ),
    ]
