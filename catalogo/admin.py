from django.contrib import admin
from .models import Libro


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "genero", "anio", "precio", "stock", "bestseller")
    list_filter = ("genero", "bestseller")
    search_fields = ("titulo", "autor")
