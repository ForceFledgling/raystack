# CLI commands

All commands are available as `raystack <command>` or `python manage.py <command>`.

## Core
- `startproject <name> [--with-home/--no-home]` - create a project scaffold. By default includes a minimal `app` with API and demo data.
- `startapp <name>` - create an app scaffold inside the project.
- `runserver [addr:port] [--reload]` - run the Uvicorn dev server with OpenAPI.
- `shell` - interactive Python shell with project paths set up.

## Database
- `makemigrations` - generate migrations for models (Alebmic template).
- `migrate` - apply migrations to the database.

## Users
- `createsuperuser [--username ... --email ... --noinput]` - create a superuser. Requires a User/Account app with `hash_password` in `INSTALLED_APPS`.

## Tips
- `--reload` in `runserver` watches for code changes.
- For async DB mode use an async driver in `DATABASES["default"]["URL"]`.
- All commands honor `RAYSTACK_SETTINGS_MODULE` (defaults to `config.settings` via manage.py).
