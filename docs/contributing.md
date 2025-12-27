# Contributing and development

## Local setup
```bash
git clone https://github.com/ForceFledgling/raystack.git
cd raystack
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]  # if extras are defined
```

## Tests and quality
- The project does not yet have a full test matrix; run linters/tests you add.
- Smoke test the dev server: `python manage.py runserver --reload`.

## Documentation (MkDocs)
- Install: `pip install mkdocs mkdocs-material`
- Preview: `mkdocs serve`
- Build: `mkdocs build`

## Pull Request checklist
- Update docs when behavior changes.
- Check `/docs` and the sample API.
- Avoid committing secrets in settings.
