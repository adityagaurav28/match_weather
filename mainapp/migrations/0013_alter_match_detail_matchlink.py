# Generated by Django 3.2.4 on 2021-07-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20210703_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match_detail',
            name='matchLink',
            field=models.CharField(default='NULL', max_length=500),
        ),
    ]