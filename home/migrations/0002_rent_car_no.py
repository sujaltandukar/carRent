# Generated by Django 3.0.3 on 2020-03-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='car_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
