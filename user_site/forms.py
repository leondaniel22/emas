from django import forms
from .models import *


class SolutionForm(forms.Form):
    err_app = forms.IntegerField()


class SuccessForm(forms.Form):
    sol = forms.IntegerField()


class AppearanceForm(forms.Form):
    location = forms.CharField(max_length=70)


class RequestCommentForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control'
        }),
        label="Vorschlag")


class EditCommentForm(forms.Form):
    REASONS = (
        ("1", "Lösung hat garnicht nicht geholfen"),
        ("2", "Lösung hat nur teilweise geholfen"),
        ("3", "Lösung passt nicht zum Fehler"),
        ("4", "sonstiges"),
    )
    MEDIA_VALIDATION = (
        ("1", "Das Bild/Video war nicht hilfreich"),
        ("2", "Das Bild/Video war teilweise hilfreich"),
        ("3", "Das Bild/Video war nicht hilfreich"),
        ("4", "keine Angabe"),
    )

    reason = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': 'form-control w-25',
        }),
        choices=REASONS,
        label="Allgemeines")

    media_validation = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': 'form-control w-25',
        }),
        choices=MEDIA_VALIDATION,
        label="Bild/Video")

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control'
        }),
        label="Vorschlag")


