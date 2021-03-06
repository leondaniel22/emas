# Generated by Django 3.2.6 on 2021-09-12 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0022_auto_20210912_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='overview',
            name='error_appearance',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='user_site.errorappearance', verbose_name='Erscheinungsbild'),
        ),
        migrations.AddField(
            model_name='overview',
            name='solution',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='user_site.solution', verbose_name='Lösung'),
        ),
    ]
