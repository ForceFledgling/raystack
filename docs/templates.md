# Templates and static files

Raystack does not force templates by default but supports Jinja2 and Django-like static handling.

## Enable Jinja2
In `config/settings.py` uncomment `TEMPLATES`:
```python
TEMPLATES = [
    {
        "BACKEND": "raystack.template.backends.jinja2.Jinja2",
        "DIRS": ["templates", "jinja2"],
        "APP_DIRS": True,
    },
]
```
Create a `templates/` folder and add `.html` files.

## Render from a view
```python
from raystack.shortcuts import render

@router.get("/hello")
async def hello(request: Request):
    return render(request, "hello.html", {"name": "Raystack"})
```

## Static files
- URL prefix: `STATIC_URL = "static/"`
- Directories: `STATICFILES_DIRS = [BASE_DIR / "static"]`
Raystack mounts the first existing directory under `STATIC_URL`.

## When templates are not needed
Templates are optional: by default the API returns JSON and works without Jinja2.
