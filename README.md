# Сucumber
Cucumber food delivery project. Backend and landing page.

[![Linting](https://github.com/lamedevelop/cucumber/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/lamedevelop/cucumber/actions/workflows/ci.yml)
---

### Quickstart

You must have docker and docker-compose tools 
installed to run the application. 
Simply you can just run following command.


Run full project from project root:
```bash
make docker
```

Or run docker-compose manually:

```bash
docker-compose up -d --build
```

Also you can run parts of application separately.
It's useful for debugging.

1. Install requirements
2. Run db container with: 
```make db```
3. Run alembic migrations:
```make alembic```
4. Run app locally:
```make local```

[Up](#cucumber)


### What's inside

All web routes of the app available on /docs path.

Project structure presented below:

```
app
├── api              - routing and web related modules
│
├── db               - db related modules
│   ├── migrations   - generated alembic migrations
│   └── models       - db models
│   └── schema.py    - description of db structure
│
├── internal         - internal modules
│
└── main.py          - FastAPI application: creation and configuration
```

[Up](#cucumber)
