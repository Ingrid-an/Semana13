"""URLs del proyecto: API, admin y documentación OpenAPI/Swagger."""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("catalogo.urls")),
    # Fase 5: documentación automática
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # login de la API navegable
    path("api-auth/", include("rest_framework.urls")),
]
