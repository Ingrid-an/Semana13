"""Fase 3 y 4: ViewSet, filtros, paginación y throttling."""
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Libro
from .serializers import LibroSerializer


class LibroViewSet(viewsets.ModelViewSet):
    """CRUD completo de libros vía ModelViewSet.

    El Router genera automáticamente: GET list/retrieve, POST create,
    PUT/PATCH update, DELETE destroy.
    """
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # lectura pública, escritura autenticada

    # Fase 4: backends de filtrado
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["genero", "autor", "bestseller"]      # ?genero=romance&bestseller=true
    search_fields = ["titulo", "autor"]                       # ?search=king
    ordering_fields = ["precio", "anio", "creado"]            # ?ordering=-precio
    ordering = ["-creado"]

    # Fase 3: endpoint custom con @action
    @action(detail=False, methods=["get"])
    def bestsellers(self, request):
        """GET /api/libros/bestsellers/ — solo los bestsellers."""
        qs = self.get_queryset().filter(bestseller=True)
        page = self.paginate_queryset(qs)
        serializer = self.get_serializer(page or qs, many=True)
        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)
