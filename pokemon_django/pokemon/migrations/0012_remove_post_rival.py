# Generated by Django 4.0 on 2021-12-17 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0011_post_rival'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='rival',
        ),
    ]
