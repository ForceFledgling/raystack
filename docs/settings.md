# Settings

Raystack uses a settings module defined by `RAYSTACK_SETTINGS_MODULE` (default `config.settings`). Base values come from `raystack.conf.global_settings` and are overridden by your file.

## Key options
- `INSTALLED_APPS`: app paths that expose routers.
- `DATABASES`: DB configuration; can be empty if you do not use a DB.
- `ALLOWED_HOSTS`: hosts allowed in production.
- `DEBUG`: toggles debug mode.
- `STATIC_URL`, `STATICFILES_DIRS`: static asset locations.
- `DOCS_URL`, `OPENAPI_URL`: Swagger/UI and schema URLs.
- `API_TITLE`, `API_VERSION`, `API_DESCRIPTION`: OpenAPI metadata.
- `MIDDLEWARE`: list of middleware classes (full paths).

## Setting via env
Set `RAYSTACK_SETTINGS_MODULE` before running:
```bash
export RAYSTACK_SETTINGS_MODULE="myproject.config.settings"
python manage.py runserver
```

## Tips
- Raystack mounts the first existing directory from `STATICFILES_DIRS`.
- If `DEBUG` is false, fill in `ALLOWED_HOSTS`.
- For Jinja2 enable the `TEMPLATES` block in settings.
