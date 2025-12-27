# Documentation and OpenAPI

Raystack wires up OpenAPI and Swagger UI automatically.

- Swagger UI: `DOCS_URL` (default `/docs`)
- OpenAPI JSON: `OPENAPI_URL` (default `/openapi.json`)

## What is generated
- All routes from `INSTALLED_APPS` are included in the schema.
- Path params (`{item_id}`) are added even if not present in the function signature (Starlette passes them via `request.path_params`).
- Request bodies with Pydantic models are published as forms (`application/x-www-form-urlencoded` and `multipart/form-data`) for easy testing in Swagger.

## Customization
In `config/settings.py` you can set:
```python
DOCS_URL = "/docs"
OPENAPI_URL = "/openapi.json"
API_TITLE = "My API"
API_VERSION = "0.1.0"
API_DESCRIPTION = "Internal services"
```

## FAQ
- **Why no JSON body in Swagger?** The generator emits forms for easier manual testing. JSON is still accepted if you parse `await request.json()` in the handler.
- **Why are path params absent in the signature?** `APIRouter` is a Starlette wrapper; parameters are available via `request.path_params`.
