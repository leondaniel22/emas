from django import forms
from .models import *


class SolutionForm(forms.Form):
    err_app = forms.IntegerField()


class SuccessForm(forms.Form):
    sol = forms.IntegerField()


class AppearanceForm(forms.Form):
    location = forms.CharField(max_length=70)


class RequestCommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label="Vorschlag")


class EditCommentForm(forms.Form):
    content = forms.Textarea()
