# Generated by Django 2.0.7 on 2018-09-01 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeb_app', '0023_auto_20180901_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='zakup',
            name='year',
            field=models.ForeignKey(default=2000, null=True, on_delete=django.db.models.deletion.CASCADE, to='homeb_app.Rok'),
        ),
    ]
