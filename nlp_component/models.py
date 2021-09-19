from django.db import models
from user_site.models import *
from user_site.forms import *
# Create your models here.


class Comment(models.Model):

    content = models.TextField("Inhalt", max_length=5000, default="")

    class Meta:
        verbose_name = "Kommentar"
        verbose_name_plural = "Kommentare"


class RequestComment(Comment, models.Model):
    error_appearance = models.ForeignKey(verbose_name="Erscheinungsbild", to=ErrorAppearance, on_delete=models.CASCADE,
                                         default=None, blank=True)

    class Meta:
        verbose_name = "Neuer Lösungsvorschlag"
        verbose_name_plural = "Neue Lösungsvorschläge"


class EditComment(Comment, models.Model):
    solution = models.ForeignKey(verbose_name="Lösung", to=Solution, on_delete=models.CASCADE,
                                         default=None)
    reason = models.CharField(verbose_name="Grund", max_length=2, choices=EditCommentForm.REASONS, default=None)
    media_validation = models.CharField(verbose_name="Bild/Video Bewertung", max_length=2, choices=EditCommentForm.MEDIA_VALIDATION, default=None)
    class Meta:
        verbose_name = "Überarbeiteter Lösungsvorschlag"
        verbose_name_plural = "Überarbeitete Lösungsvorschläge"