# Generated by Django 3.0.6 on 2021-09-18 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated',
        ),
    ]