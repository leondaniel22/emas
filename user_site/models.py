from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType
from dbview.models import DbView
# Create your models here.


class ErrorCategory(models.Model):
    name = models.CharField("Name", max_length=200)
    description = models.CharField("Beschreibung", max_length=500, default="Keine spezifische Beschreibung vorhanden")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fehlerkategorie"
        verbose_name_plural = " Fehlerkategorien"


class Location(models.Model):
    name = models.CharField("Name", max_length=200)
    description = models.CharField("Beschreibung", max_length=500, default="Keine spezifische Beschreibung vorhanden")
    pdf_document = models.FileField("PDF Dokument", upload_to='locations/', default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fehlerort"
        verbose_name_plural = "Fehlerorte"


class ErrorAppearance(models.Model):


    name = models.CharField("Name", max_length=200)
    description = models.CharField("Beschreibung", max_length=500, default="Keine spezifische Beschreibung vorhanden")
    location = models.ForeignKey(verbose_name="Fehlerort", to=Location, on_delete=models.CASCADE)
    media = models.FileField("Bild/Video", upload_to='error_appearances/', default="error_appearances/coming-soon.png")
    error_category = models.ForeignKey(verbose_name="Fehlerkategorie", to=ErrorCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Erscheinungsbild"
        verbose_name_plural = "Erscheiungsbilder"

class Solution(models.Model):
    name = models.CharField("Name", max_length=200)
    description = models.CharField("Beschreibung", max_length=500, default="Keine spezifische Beschreibung vorhanden")
    media = models.FileField("Bild/Video", upload_to='solutions/', default="solutions/coming-soon.png")
    rating = models.IntegerField("Rating", default=0)
    error_appearance = models.ForeignKey(verbose_name="Erscheinungsbild",to=ErrorAppearance, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "L??sung"
        verbose_name_plural = "L??sungen"


class Overview(models.Model):

    class Meta:
        app_label = 'user_site'
        verbose_name = "??bersicht"
        verbose_name_plural = "  ??bersicht"

class Import(models.Model):

    class Meta:
        app_label = 'user_site'
        verbose_name = 'Excel Import'
        verbose_name_plural = ' Excel Import'