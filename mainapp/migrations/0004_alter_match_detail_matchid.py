# Generated by Django 3.2.4 on 2021-06-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210629_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match_detail',
            name='matchId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]