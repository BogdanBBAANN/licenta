# Generated by Django 3.1.7 on 2021-03-04 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20210227_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]