# Generated by Django 5.0.2 on 2024-02-23 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricing',
            old_name='item',
            new_name='item_id',
        ),
        migrations.RenameField(
            model_name='pricing',
            old_name='organization',
            new_name='organization_id',
        ),
    ]