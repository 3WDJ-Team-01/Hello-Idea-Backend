# Generated by Django 2.1.5 on 2019-04-19 05:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190418_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Root_idea',
            fields=[
                ('Root_idea_id', models.AutoField(primary_key=True, serialize=False)),
                ('idea_cont', models.CharField(max_length=50)),
                ('idea_color', models.CharField(max_length=50)),
                ('idea_height', models.FloatField()),
                ('idea_width', models.FloatField()),
            ],
            options={
                'db_table': 'Root_idea',
            },
        ),
        migrations.AlterField(
            model_name='idea',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 19, 5, 38, 11, 880584, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 19, 5, 38, 11, 878589, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='root_idea',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Project'),
        ),
    ]
