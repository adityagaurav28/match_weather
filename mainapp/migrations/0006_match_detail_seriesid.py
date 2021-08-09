# Generated by Django 3.2.4 on 2021-06-29 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_series_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='match_detail',
            name='seriesId',
            field=models.ForeignKey(db_column='seriesId', default=1001, on_delete=django.db.models.deletion.CASCADE, to='mainapp.series_detail'),
            preserve_default=False,
        ),
    ]