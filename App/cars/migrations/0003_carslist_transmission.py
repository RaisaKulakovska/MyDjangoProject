# Generated by Django 3.0.4 on 2020-03-31 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20200326_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='carslist',
            name='transmission',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]