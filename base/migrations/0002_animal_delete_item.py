# Generated by Django 4.1.7 on 2023-08-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=True)),
                ('lat', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]