# Generated by Django 2.0.8 on 2018-08-31 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeb_app', '0017_auto_20180831_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakup',
            name='year',
            field=models.ForeignKey(default=2000, on_delete=django.db.models.deletion.CASCADE, to='homeb_app.Rok'),
        ),
    ]