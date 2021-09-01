# containered-services

## Basic configuration
Create a `.env` file in the root of the project and add a `DATABASE_URL` variable,
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