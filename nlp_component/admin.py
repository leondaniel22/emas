from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(RequestComment)
class RequestCommentAdmin(admin.ModelAdmin):
    list_display = ("content", "error_appearance")

@admin.register(EditComment)
class EditCommentAdmin(admin.ModelAdmin):
    list_display = ("content", "solution")