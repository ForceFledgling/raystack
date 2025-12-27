# Data and ORM (optional)

The project template starts without a database and keeps demo data in memory. When you need persistence, turn on the Raystack ORM.

## Enable the database
1) In `config/settings.py` uncomment/configure `DATABASES`:
```python
DATABASES = {
    "default": {
        "ENGINE": "raystack.core.database.sqlalchemy",
        "URL": "sqlite:///db.sqlite3",  # or async URL: sqlite+aiosqlite:///...
    }
}
```
2) In `app/models.py` uncomment the sample model or add your own:
```python
from raystack.core.database.models import Model
from raystack.core.database.fields import AutoField, CharField

class ItemModel(Model):
    table = "example_item"
    id = AutoField()
    name = CharField(max_length=100, unique=True)
    description = CharField(max_length=100)
```
3) Generate and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Use in API
```python
@router.get("/", response_model=list[Item])
async def list_items(request: Request):
    items = await ItemModel.objects.all()
    return JSONResponse([Item.from_orm(obj).dict() for obj in items])
```

## Sync vs async mode
The driver in `URL` decides:
- sync: `sqlite:///...`, `postgresql://...`, `mysql://...`
- async: `sqlite+aiosqlite://...`, `postgresql+asyncpg://...`, `mysql+aiomysql://...`

## Tips
- Keep the API in-memory until you truly need a DB.
- `sqlite3.OperationalError` is wrapped into 500 with a hint to run `makemigrations/migrate`.
- Migrations use the Alembic scaffold generated with the project.
