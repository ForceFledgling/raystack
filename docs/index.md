# Raystack - Starlette speed with Django-style ergonomics

Raystack is a light ASGI framework on top of Starlette with a Django-like project structure: `startproject`/`startapp`, settings, routers, templates, and CLI commands. It ships with a minimal in-memory API so you can see a response without setting up a database, and lets you turn on ORM, templates, and middleware when you need them.

## Why Raystack
- Starlette under the hood: fast and async-friendly.
- Django-like ergonomics: `INSTALLED_APPS`, settings, manage-style commands, templates, static files.
- Auto docs: Swagger UI at `/docs`, OpenAPI at `/openapi.json`.
- Minimal first run: working in-memory API with no DB required.
- Extensible: plug in ORM, middleware, Jinja2, and custom commands as you grow.

## Quick start
```bash
pip install "mkdocs-material" "raystack"  # Raystack + docs tooling
raystack startproject myproject && cd myproject
python manage.py runserver --reload
# Open: http://127.0.0.1:8000 and http://127.0.0.1:8000/docs
```

See "Getting started" and "Routing" for more detail.

## What's inside
- CLI: `startproject`, `startapp`, `runserver`, `makemigrations`, `migrate`, `shell`, `createsuperuser`.
- Routers: `raystack.compat.APIRouter` with Starlette-compatible semantics.
- Templates and static files: configured via `TEMPLATES` and `STATICFILES_DIRS`.
- OpenAPI: schema + Swagger UI out of the box.
- Sample API: `/api/items` with in-memory data so you can test immediately.

Next: read "Getting started" or dive into "Routing and requests."
