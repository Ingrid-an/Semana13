"""Fase 2: serialización avanzada de la API de Biblioteca."""
from rest_framework import serializers
from .models import Libro


class LibroSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer hipervinculado (HATEOAS): incluye enlaces de navegación."""

    # Campo calculado de solo lectura (SerializerMethodField)
    disponible = serializers.SerializerMethodField()
    # Campo de solo lectura directo (ReadOnlyField)
    genero_display = serializers.ReadOnlyField(source="get_genero_display")

    class Meta:
        model = Libro
        # 'url' da el enlace HATEOAS a cada recurso
        fields = ["url", "id", "titulo", "autor", "genero", "genero_display",
                  "anio", "precio", "stock", "disponible", "bestseller", "creado"]
        read_only_fields = ["creado"]
        extra_kwargs = {
            "url": {"view_name": "libro-detail"},
        }

    def get_disponible(self, obj):
        """Campo calculado: True si hay stock."""
        return obj.stock > 0

    def validate_anio(self, value):
        """Validación de campo: año razonable."""
        if value < 1400 or value > 2100:
            raise serializers.ValidationError("El año debe estar entre 1400 y 2100.")
        return value

    def validate_precio(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio no puede ser negativo.")
        return value

    def validate(self, data):
        """Validación a nivel de objeto (cross-field):
        un bestseller debe tener stock disponible."""
        bestseller = data.get("bestseller", getattr(self.instance, "bestseller", False))
        stock = data.get("stock", getattr(self.instance, "stock", 0))
        if bestseller and stock == 0:
            raise serializers.ValidationError(
                "Un bestseller no puede estar sin stock.")
        return data
