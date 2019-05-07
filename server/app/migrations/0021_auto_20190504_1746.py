# Generated by Django 2.1.5 on 2019-05-04 08:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20190504_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='idea',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 8, 46, 49, 194061, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 8, 46, 49, 193007, tzinfo=utc)),
        ),
    ]
