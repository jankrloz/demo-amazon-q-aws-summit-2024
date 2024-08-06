from app.config.db import Session
from app.models import User


class UserService:
    def create_user(self, name: str):
        new_user = User(name=name)
        with Session() as session:
            session.add(new_user)
            session.commit()
        return new_user

    def get_users(self):
        with Session() as session:
            users = session.query(User).all()
        return users
