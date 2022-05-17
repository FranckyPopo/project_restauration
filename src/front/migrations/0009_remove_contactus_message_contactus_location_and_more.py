# Generated by Django 4.0.4 on 2022-05-17 12:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0008_avisclient_photo_client_alter_aboutindex_date_create_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='message',
        ),
        migrations.AddField(
            model_name='contactus',
            name='location',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutindex',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 12, 10, 40, 396728, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='addmenu',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 12, 10, 40, 396393, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='avisclient',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 12, 10, 40, 397385, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='backgroundimageindex',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 12, 10, 40, 395774, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booktable',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 12, 10, 40, 397083, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 12, 10, 40, 397730, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sliderindex',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 12, 10, 40, 395038, tzinfo=utc)),
        ),
    ]
