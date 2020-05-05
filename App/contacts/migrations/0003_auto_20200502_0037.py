# Generated by Django 3.0.4 on 2020-05-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200421_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]