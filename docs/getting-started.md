# Getting started

## Requirements
- Python 3.9+ (virtualenv recommended)
- pip

## Install
```bash
python -m venv .venv && source .venv/bin/activate  # optional
pip install "raystack"
```

## Create a project
```bash
raystack startproject myproject
cd myproject
```
The scaffold ships with a minimal API and in-memory data; no DB required.

## Run the dev server
```bash
python manage.py runserver 0.0.0.0:8000 --reload
```
- Swagger UI: http://127.0.0.1:8000/docs
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json
- Demo API: http://127.0.0.1:8000/api/items

## Settings
`manage.py` sets `RAYSTACK_SETTINGS_MODULE=config.settings`. Key options in `config/settings.py`:
- `INSTALLED_APPS` - your apps (defaults to `app`).
- `DATABASES` - keep or comment out; optional for DB-free start.
- `STATIC_URL`, `STATICFILES_DIRS` - static assets.
- `DOCS_URL`, `OPENAPI_URL` - docs endpoints.

## Next steps
- Create a new app: `python manage.py startapp blog` and add it to `INSTALLED_APPS`.
- Review the scaffold in "Project structure."
- Add routes - see "Routing and requests."
- Enable DB/ORM - see "Data and ORM."
