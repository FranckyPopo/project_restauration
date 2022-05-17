# Generated by Django 4.0.4 on 2022-05-17 14:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0010_linkreseau_date_create_alter_aboutindex_date_create_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmenu',
            name='type_food',
            field=models.CharField(choices=[('burger', 'Burger'), ('pizza', 'Pizza'), ('pasta', 'Pasta'), ('fries', 'Fries')], default='Burger', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutindex',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 14, 36, 14, 488902, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='addmenu',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 14, 36, 14, 488500, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='avisclient',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 14, 36, 14, 489602, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='backgroundimageindex',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 14, 36, 14, 487878, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booktable',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 14, 36, 14, 489285, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 14, 36, 14, 490084, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='linkreseau',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 14, 36, 14, 490412, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sliderindex',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 14, 36, 14, 487148, tzinfo=utc)),
        ),
    ]