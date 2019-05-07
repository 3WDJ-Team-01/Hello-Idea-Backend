# Generated by Django 2.1.5 on 2019-05-02 02:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20190502_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 2, 36, 34, 346430, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_img',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 2, 36, 34, 344437, tzinfo=utc)),
        ),
    ]