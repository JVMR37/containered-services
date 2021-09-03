# containered-services

## Basic configuration

Create a `.env` file in the root of the project and add a **DATABASE_URL** variable,
with the URL to access your database, following the
[SQLAlchemy Database Urls](https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls) specifications.

Ps.: Check the .env.template file for examples with SQLite Databases,
and PostgreSQL databases

## Installing requirements

Open a terminal in the root of the project, then type the following command:

```
pip install -r requirements.txt
```

Ps.: It is recommended that you use a [virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments).

## Starting the server

Open a terminal in the root of the project, then type the following command:

```properties
uvicorn main:app
```

## Running with docker

To work with the default configuration provided in the `docker-compose.yml`, add this line to the `.env` file:

```
DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/database
```

Open a terminal in the root of the project, then type the following commands:

```properties
docker-compose build
docker-compose up
```
