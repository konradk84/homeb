# Generated by Django 2.0.7 on 2018-09-01 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeb_app', '0034_auto_20180901_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakup',
            name='month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeb_app.Miesiac'),
        ),
    ]