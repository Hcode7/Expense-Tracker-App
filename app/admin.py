from django.contrib import admin
from .models import Category, Book
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass