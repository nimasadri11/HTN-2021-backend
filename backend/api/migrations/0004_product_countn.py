# Generated by Django 3.0.6 on 2021-09-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210918_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='countn',
            field=models.IntegerField(default=0),
        ),
    ]