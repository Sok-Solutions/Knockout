# Generated by Django 4.1.3 on 2022-11-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0017_gamesss'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesss',
            name='M',
            field=models.IntegerField(default=10),
        ),
    ]
