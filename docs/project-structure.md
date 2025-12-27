# Project structure

`startproject` generates a minimal scaffold that does not require a database.

```
myproject/
|-- app/                 # Minimal app with API and in-memory examples
|   |-- api/
|   |   |-- __init__.py  # router, healthcheck
|   |   `-- items.py     # in-memory CRUD
|   |-- __init__.py      # root router ("/")
|   |-- apps.py          # AppConfig
|   |-- models.py        # commented ORM example
|   `-- schemas.py       # Pydantic schemas
|-- config/
|   |-- settings.py      # project settings
|   `-- urls.py          # attach app routers
|-- core/__init__.py     # ASGI entrypoint: app = Raystack()
|-- manage.py            # CLI wrapper (runserver, startapp, etc.)
|-- db.sqlite3           # created if DB enabled
`-- alembic.ini          # only if migrations/ORM are enabled
```

### Key files
- `app/__init__.py` - root router (`/`), includes API.
- `app/api/items.py` - demo in-memory CRUD.
- `config/settings.py` - base settings; DB is optional.
- `core/__init__.py` - creates `Raystack()`, mounts OpenAPI and routers.

### Add a new app
```bash
python manage.py startapp blog
```
Add `blog` to `INSTALLED_APPS` and include its router in `config/urls.py`, e.g.:
```python
from blog import router as blog_router
router.include_router(blog_router, prefix="/blog", tags=["Blog"])
```
