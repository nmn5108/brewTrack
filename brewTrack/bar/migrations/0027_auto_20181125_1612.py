# Generated by Django 2.1.2 on 2018-11-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0026_auto_20181125_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='current_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='total_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]