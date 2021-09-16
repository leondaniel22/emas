from django.contrib import admin
from .models import *
from django.shortcuts import render, redirect
import datetime
from datetime import datetime
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import *
from django.template.response import TemplateResponse
from django.urls import path
from .forms import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
@admin.register(ErrorCategory)
class ErrorCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("name", "description")


@admin.register(ErrorAppearance)
class ErrorAppearanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("name", "description", "location", "error_category")

@admin.register(Solution)
class SolutionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("name", "description", "rating", "error_appearance")



def overview(request):
    query = Solution.objects.select_related('error_appearance', 'error_appearance__error_category')
    subtitle = "Übersicht aller Verknüpfungen zwischen Fehlerkategorien, zugehöriger Erscheinungsbilder und dazu vorhandener Lösungen"
    title = 'Übersicht'
    return render(
        request,
        'admin/overview.html',
        {
            'title': title,
            'query': query,
            'has_permission': True
        }
    )


@admin.register(Overview)
class AdminOverview(admin.ModelAdmin):

    def get_urls(self):
        view = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)

        return [
            path('admin/', overview, name=view),
        ]


def import_excel(request):
    title = "Excel Import"
    user = request.user
    return render(
        request,
        'admin/import_excel.html',
        {
            'title': title,
            'has_permission': True
        }
    )


@admin.register(Import)
class AdminOverview(admin.ModelAdmin):

    def get_urls(self):
        view = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)

        return [
            path('admin/', import_excel, name=view),
        ]
