# Generated by Django 3.2.4 on 2021-06-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_match_detail_matchid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series_Detail',
            fields=[
                ('seriesId', models.AutoField(primary_key=True, serialize=False)),
                ('seriesName', models.CharField(max_length=100)),
            ],
        ),
    ]