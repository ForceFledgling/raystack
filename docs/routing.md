# Routing and requests

Raystack uses `raystack.compat.APIRouter` (a thin wrapper over Starlette Router). It takes Starlette-compatible arguments and is wired into `Raystack()` through `config/urls.py` and `INSTALLED_APPS`.

## Basic example
```python
from raystack.compat import APIRouter, JSONResponse, Request
from app.schemas import Item, ItemCreate

router = APIRouter(prefix="/api/items", tags=["Items"])

@router.get("/", response_model=list[Item])
async def list_items(request: Request):
    return JSONResponse([...])
```

## Path parameters
Starlette passes values via `request.path_params` rather than positional args. Use:
```python
@router.get("/{item_id}")
async def get_item(request: Request):
    item_id = int(request.path_params["item_id"])
    ...
```
The OpenAPI generator adds these path params to Swagger, so you will see a field for `item_id`.

## Request bodies
`BaseModel` annotations produce a request body. The OpenAPI generator publishes form-based bodies:
```python
@router.post("/", response_model=Item)
async def create_item(request: Request, item: ItemCreate):
    ...
```
Swagger offers `application/x-www-form-urlencoded` / `multipart/form-data`. You can still read JSON or forms manually:
```python
payload = await request.json()
# or
form = await request.form()
```

## Responses
Use Starlette-compatible responses from `raystack.compat`:
- `JSONResponse(content=...)`
- `HTMLResponse`, `RedirectResponse`, `Response`

## Including routers
Inside an app:
```python
# app/api/__init__.py
from raystack.compat import APIRouter
from app.api import items

router = APIRouter(prefix="/api", tags=["Example"])
router.include_router(items.router, prefix="/items", tags=["Items"])
```
In the project (`config/urls.py`) import and include your app router via `router.include_router(...)`.
