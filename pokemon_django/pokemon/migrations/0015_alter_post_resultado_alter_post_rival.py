# Generated by Django 4.0 on 2021-12-18 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0014_post_resultado_alter_post_rival'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resultado',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='rival',
            field=models.CharField(default='Salvador', max_length=100),
        ),
    ]