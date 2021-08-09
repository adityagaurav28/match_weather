# Generated by Django 3.2.4 on 2021-07-03 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_match_detail_matchweathertime'),
    ]

    operations = [
        migrations.AddField(
            model_name='match_detail',
            name='matchCurrentCloud',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match_detail',
            name='matchCurrentCondition',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='match_detail',
            name='matchCurrentHumidity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match_detail',
            name='matchCurrentTemp',
            field=models.FloatField(default=30),
        ),
    ]