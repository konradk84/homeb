# Generated by Django 2.0.7 on 2019-03-23 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeb_app', '0032_auto_20180901_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakup',
            name='month',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='homeb_app.Miesiac'),
        ),
    ]
