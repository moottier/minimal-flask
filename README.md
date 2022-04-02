# Flask Minimal Structure
A minimal set of files, folders, and utility scripts for a new Flask REST API.

Supports SQLAlchemy ORM, migrations, logging, caching

# Setup
```
git clone https://github.com/moottier/minimal-flask.git
cd minimal-flask
./setup
```

`./setup` will setup a virtual environment and install dependencies.

`./createdb` will create an SQLite3 DB, initialize alembic, migrate, then upgrade.

# Tests
`./test` or `./test -v` for verbose testing.

# Startup
Run in production mode with `./start production` or testing mode with `./start`
