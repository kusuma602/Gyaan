# Generated by Django 2.2.1 on 2020-07-23 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gyaan', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DomainTag',
            new_name='Tag',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag_name',
            new_name='name',
        ),
    ]
