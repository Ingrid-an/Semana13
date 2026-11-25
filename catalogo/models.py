"""Modelos de la API de Biblioteca."""
from django.db import models


class Libro(models.Model):
    """Libro del catálogo de la biblioteca."""

    GENEROS = [
        ("ficcion", "Ficción"), ("romance", "Romance"), ("fantasia", "Fantasía"),
        ("scifi", "Ciencia ficción"), ("clasico", "Clásico"),
        ("misterio", "Misterio"), ("infantil", "Infantil"),
    ]

    titulo = models.CharField("Título", max_length=200)
    autor = models.CharField("Autor", max_length=120)
    genero = models.CharField("Género", max_length=20, choices=GENEROS, default="ficcion")
    anio = models.PositiveIntegerField("Año de publicación")
    precio = models.DecimalField("Precio (S/)", max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField("Stock", default=0)
    bestseller = models.BooleanField("Bestseller", default=False)
    creado = models.DateTimeField("Registrado", auto_now_add=True)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["-creado"]
        indexes = [
            models.Index(fields=["genero"]),   # índice DB para filtros frecuentes
            models.Index(fields=["autor"]),
        ]

    def __str__(self):
        return f"{self.titulo} — {self.autor}"

    @property
    def disponible(self):
        return self.stock > 0
