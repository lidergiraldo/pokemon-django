# Generated by Django 4.0 on 2021-12-16 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0008_alter_post_rival'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rival',
            field=models.CharField(default='Brock', max_length=100),
        ),
    ]