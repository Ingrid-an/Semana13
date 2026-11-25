"""python manage.py seed_data — puebla libros de prueba."""
from django.core.management.base import BaseCommand
from catalogo.models import Libro


class Command(BaseCommand):
    help = "Puebla la base de datos con libros de ejemplo."

    def handle(self, *args, **opts):
        Libro.objects.all().delete()
        datos = [
            ("Fairy Tale", "Stephen King", "fantasia", 2022, 59.00, 12, True),
            ("The Ballad of Never After", "Stephanie Garber", "fantasia", 2022, 49.00, 8, True),
            ("Klara and the Sun", "Kazuo Ishiguro", "scifi", 2021, 55.00, 15, True),
            ("A Court of Mist and Fury", "Sarah J. Maas", "fantasia", 2016, 62.00, 20, True),
            ("Hamnet", "Maggie O'Farrell", "ficcion", 2020, 48.00, 10, True),
            ("1984", "George Orwell", "clasico", 1949, 35.00, 30, False),
            ("Cien años de soledad", "Gabriel García Márquez", "clasico", 1967, 42.00, 25, False),
            ("It", "Stephen King", "misterio", 1986, 58.00, 0, False),
            ("Orgullo y prejuicio", "Jane Austen", "romance", 1813, 38.00, 18, False),
            ("El principito", "Antoine de Saint-Exupéry", "infantil", 1943, 29.00, 40, False),
            ("Dune", "Frank Herbert", "scifi", 1965, 65.00, 14, True),
            ("La sombra del viento", "Carlos Ruiz Zafón", "misterio", 2001, 45.00, 9, False),
        ]
        for t, a, g, y, p, s, b in datos:
            Libro.objects.create(titulo=t, autor=a, genero=g, anio=y,
                                 precio=p, stock=s, bestseller=b)
        self.stdout.write(self.style.SUCCESS(f"OK: {Libro.objects.count()} libros creados."))
