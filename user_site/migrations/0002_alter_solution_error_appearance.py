# Generated by Django 3.2.6 on 2021-08-03 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='error_appearance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_site.errorappearance'),
        ),
    ]
