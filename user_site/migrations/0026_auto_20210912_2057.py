# Generated by Django 3.2.6 on 2021-09-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0025_alter_overview_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Import',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Excel Import',
                'verbose_name_plural': 'Excel Import',
            },
        ),
        migrations.AlterModelOptions(
            name='overview',
            options={'verbose_name': 'Übersicht', 'verbose_name_plural': 'Übersicht'},
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]