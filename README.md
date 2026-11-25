# API Biblioteca — Django REST Framework (Semana 13)

**Asignatura:** Desarrollo de Aplicaciones Web (IS093A) · Unidad II — Desarrollo Web Fullstack
**Tema:** APIs RESTful con DRF: serialización, ViewSets, routers, paginación, filtrado, throttling, CORS/CSRF y HATEOAS.
**Autora:** Ingrid Ivette Andrade Egoavil

API RESTful de una biblioteca de libros, lista para producción, construida con
Django REST Framework.

---

## Estructura

```
biblioteca_api/
├── manage.py
├── requirements.txt
├── .gitignore
├── pruebas.rest             peticiones de prueba (REST Client)
├── config/
│   ├── settings.py          DRF, CORS, Spectacular, throttling, paginación
│   └── urls.py              router + Swagger/Redoc
└── catalogo/
    ├── models.py            modelo Libro (con índices DB)
    ├── serializers.py       Hyperlinked + SerializerMethodField + validate()
    ├── views.py             LibroViewSet (ModelViewSet) + @action
    ├── urls.py              DefaultRouter
    ├── admin.py
    └── management/commands/seed_data.py
```

---

## Cumplimiento de las 5 fases

- **Fase 1 — Setup DRF:** `rest_framework`, `django_filters`, `corsheaders`,
  `drf_spectacular` en INSTALLED_APPS; bloque `REST_FRAMEWORK` con paginación,
  throttling y auth; `CORS_ALLOWED_ORIGINS`; `SPECTACULAR_SETTINGS`.
- **Fase 2 — Serialización:** `LibroSerializer` (HyperlinkedModelSerializer →
  HATEOAS con campo `url`), `SerializerMethodField` (`disponible`),
  `ReadOnlyField` (`genero_display`), `validate_<campo>()` y `validate()` objeto.
- **Fase 3 — ViewSets & Routers:** `LibroViewSet(ModelViewSet)` + `DefaultRouter`
  (CRUD automático); `@action` custom `bestsellers`.
- **Fase 4 — Filtrado, Paginación, Throttling:** `DjangoFilterBackend`,
  `SearchFilter`, `OrderingFilter`; `PageNumberPagination` (5/pág);
  `AnonRateThrottle` (30/min) y `UserRateThrottle` (100/min).
- **Fase 5 — CORS, CSRF & Docs:** `corsheaders` middleware, orígenes permitidos;
  documentación OpenAPI en `/api/docs/` (Swagger) y `/api/redoc/`.

---

## Cómo ejecutar (paso a paso)

Requiere **Python 3.11+**.

```bash
# 1. (opcional) entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows

# 2. instalar dependencias
pip install -r requirements.txt

# 3. migraciones
python manage.py makemigrations
python manage.py migrate

# 4. poblar libros de prueba
python manage.py seed_data

# 5. superusuario (para crear/editar vía API navegable y admin)
python manage.py createsuperuser

# 6. arrancar
python manage.py runserver
```

---

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/api/libros/` | Lista (paginada) |
| POST | `/api/libros/` | Crear (autenticado) |
| GET | `/api/libros/{id}/` | Detalle |
| PUT/PATCH | `/api/libros/{id}/` | Actualizar (autenticado) |
| DELETE | `/api/libros/{id}/` | Eliminar (autenticado) |
| GET | `/api/libros/bestsellers/` | Solo bestsellers (@action) |
| GET | `/api/docs/` | Documentación Swagger |
| GET | `/api/redoc/` | Documentación Redoc |
| GET | `/api/schema/` | Esquema OpenAPI (YAML) |

### Query params (Fase 4)
```
?genero=fantasia          filtrar por género
?bestseller=true          filtrar por bestseller
?search=king              buscar en título/autor
?ordering=-precio         ordenar (- = descendente)
?page=2                   paginación
```

---

## Notas de la rúbrica
- Lectura pública, escritura autenticada (`IsAuthenticatedOrReadOnly`).
- Throttling activo contra abuso.
- No se exponen campos sensibles; validación en el serializador.
- `db.sqlite3` y `.env` en `.gitignore` (no se suben).
- `python manage.py check` sin problemas.
