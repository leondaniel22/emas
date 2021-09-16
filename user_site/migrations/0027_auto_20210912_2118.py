# Generated by Django 3.2.6 on 2021-09-12 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0026_auto_20210912_2057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='errorcategory',
            options={'verbose_name': 'Fehlerkategorie', 'verbose_name_plural': ' Fehlerkategorien'},
        ),
        migrations.AlterModelOptions(
            name='import',
            options={'verbose_name': 'Excel Import', 'verbose_name_plural': ' Excel Import'},
        ),
        migrations.AlterModelOptions(
            name='overview',
            options={'verbose_name': 'Übersicht', 'verbose_name_plural': '  Übersicht'},
        ),
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
            name='name',
        ),
        migrations.RemoveField(
            model_name='overview',
            name='solution',
        ),
        migrations.AlterModelTable(
            name='overview',
            table=None,
        ),
    ]