# Generated by Django 2.1.1 on 2018-11-01 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0007_remove_event_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='bar',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
