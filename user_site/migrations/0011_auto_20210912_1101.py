# Generated by Django 3.2.6 on 2021-09-12 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0010_auto_20210911_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overview',
            name='error_appearance',
        ),
        migrations.RemoveField(
            model_name='overview',
            name='error_category',
        ),
        migrations.RemoveField(
            model_name='overview',
            name='solution',
        ),
    ]
