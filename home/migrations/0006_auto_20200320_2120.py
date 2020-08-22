# Generated by Django 3.0.3 on 2020-03-20 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200315_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('c_email', models.EmailField(max_length=100)),
                ('c_subject', models.CharField(max_length=100)),
                ('c_message', models.TextField(max_length=1000)),
                ('c_datesend', models.DateTimeField(auto_now_add=True, verbose_name='date send')),
            ],
        ),
        migrations.DeleteModel(
            name='ContactPost',
        ),
    ]
