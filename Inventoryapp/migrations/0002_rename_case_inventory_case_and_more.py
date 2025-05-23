# Generated by Django 4.2.4 on 2025-04-22 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventoryapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='Case',
            new_name='case',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='SKU',
            new_name='sku',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='Quantity',
        ),
        migrations.AddField(
            model_name='inventory',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
