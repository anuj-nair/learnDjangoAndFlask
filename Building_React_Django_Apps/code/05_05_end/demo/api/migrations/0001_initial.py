# Generated by Django 2.2.1 on 2019-07-16 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('promo', models.TextField()),
                ('price', models.FloatField()),
                ('rating', models.CharField(max_length=50)),
                ('tour_length', models.IntegerField()),
                ('thumbnail_url', models.CharField(max_length=200)),
            ],
        ),
    ]
