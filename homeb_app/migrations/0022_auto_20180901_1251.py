# Generated by Django 2.0.7 on 2018-09-01 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeb_app', '0021_auto_20180901_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakup',
            name='month',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='homeb_app.Miesiac'),
        ),
    ]
