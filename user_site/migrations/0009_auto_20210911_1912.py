# Generated by Django 3.2.6 on 2021-09-11 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0008_auto_20210911_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='object_id',
        ),
        migrations.AddField(
            model_name='comments',
            name='error_appearance',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user_site.errorappearance', verbose_name='Erscheinungsbild'),
        ),
        migrations.AddField(
            model_name='comments',
            name='solution',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user_site.solution', verbose_name='Lösung'),
        ),
        migrations.AddField(
            model_name='comments',
            name='type',
            field=models.CharField(choices=[('A', 'Neuer Lösungsvorschlag'), ('B', 'Kommentar zu bestehender Lösung')], default=None, max_length=1, verbose_name='Typ'),
        ),
    ]
