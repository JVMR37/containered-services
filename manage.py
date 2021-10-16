import click

from backend.entities.database.config import SessionLocal
from backend.entities.database.models import User
from backend.routers.user import security


@click.command()
def create_user_user():
    session = SessionLocal()
    user = User(username='admin', password=security.hash('admin'), role='admin')
    session.add(user)
    session.commit()

    click.echo('Created super user with the following credentials:\nusername: admin\npassword: admin')


if __name__ == '__main__':
    create_user_user()
