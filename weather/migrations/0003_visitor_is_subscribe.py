# Generated by Django 4.1 on 2022-08-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_visitor_location_visitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='is_subscribed',
            field=models.BooleanField(default=True),
        ),
    ]
