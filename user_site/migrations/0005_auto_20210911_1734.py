# Generated by Django 3.2.6 on 2021-09-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0004_auto_20210823_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Übersicht',
                'verbose_name_plural': 'Übersicht',
            },
        ),
        migrations.AddField(
            model_name='errorappearance',
            name='media',
            field=models.FileField(default='', upload_to='error_appearances/', verbose_name='Bild/Video'),
        ),
        migrations.AddField(
            model_name='solution',
            name='media',
            field=models.FileField(default='', upload_to='solutions/', verbose_name='Bild/Video'),
        ),
    ]
