# Generated by Django 4.0.7 on 2022-08-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_alter_visitor_is_subscribed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='is_subscribed',
            field=models.BooleanField(default=True),
        ),
    ]