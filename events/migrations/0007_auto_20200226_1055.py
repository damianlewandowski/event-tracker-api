# Generated by Django 3.0.3 on 2020-02-26 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20200226_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='event',
        ),
    ]
