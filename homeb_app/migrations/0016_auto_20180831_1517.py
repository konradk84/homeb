# Generated by Django 2.0.8 on 2018-08-31 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeb_app', '0015_auto_20180831_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rok',
            name='name',
            field=models.IntegerField(default=2000),
        ),
    ]
