# Generated by Django 3.2.6 on 2021-09-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlp_component', '0003_auto_20210919_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='editcomment',
            name='media_validation',
            field=models.CharField(choices=[('1', 'Das Bild/Video war nicht hilfreich'), ('2', 'Das Bild/Video war teilweise hilfreich'), ('3', 'Das Bild/Video war nicht hilfreich'), ('4', 'keine Angabe')], default=None, max_length=2, verbose_name='Bild/Video Bewertung'),
        ),
        migrations.AddField(
            model_name='editcomment',
            name='reason',
            field=models.CharField(choices=[('1', 'Lösung hat garnicht nicht geholfen'), ('2', 'Lösung hat nur teilweise geholfen'), ('3', 'Lösung passt nicht zum Fehler'), ('4', 'sonstiges')], default=None, max_length=2, verbose_name='Grund'),
        ),
    ]
