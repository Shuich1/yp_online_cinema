# Generated by Django 3.2 on 2022-12-06 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_renamed_fields_for_data_migration'),
    ]
    operations = [
        migrations.RenameField(
            model_name='genrefilmwork',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='personfilmwork',
            old_name='created',
            new_name='created_at',
        ),
    ]
