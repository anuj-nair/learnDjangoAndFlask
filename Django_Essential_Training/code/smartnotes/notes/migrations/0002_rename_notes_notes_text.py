# Generated by Django 3.2.7 on 2021-10-03 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='notes',
            new_name='text',
        ),
    ]
