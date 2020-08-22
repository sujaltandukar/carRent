# Generated by Django 3.0.3 on 2020-03-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rent_car_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='fuel',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rent',
            name='luggage',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rent',
            name='mileage',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rent',
            name='seats',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
