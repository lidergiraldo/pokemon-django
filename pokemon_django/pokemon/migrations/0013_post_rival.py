# Generated by Django 4.0 on 2021-12-17 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0012_remove_post_rival'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rival',
            field=models.CharField(default='Patrick', max_length=100),
        ),
    ]
