# Generated by Django 2.0.7 on 2018-09-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeb_app', '0030_zakup_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakup',
            name='year',
            field=models.IntegerField(),
        ),
    ]