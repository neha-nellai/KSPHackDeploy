# Generated by Django 3.0.3 on 2020-04-09 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200330_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='shared',
            name='is_folder',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shared',
            name='file',
            field=models.IntegerField(),
        ),

    ]
